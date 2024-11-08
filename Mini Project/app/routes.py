from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from .forms import RegistrationForm, LoginForm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from .models import db, Hospital
from .data_processing import process_and_upload_data
import logging
logging.basicConfig(level=logging.INFO)

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, password=hashed_password, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
@auth.route('/',methods=['POST','GET'])
def home():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Please check your login details and try again.')
    return render_template('login.html', form=form)

@auth.route('/dashboard')
@login_required
def dashboard():
    # Passing the current user to the template, so you can access 'current_user.role'
    return render_template('dashboard.html', current_user=current_user)

@auth.route('/manage_users')
@login_required
def manage_users():
    if current_user.role != 'administrator':
        return redirect(url_for('dashboard'))  
    
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@auth.route('/upload_data', methods=['POST', 'GET'])
@login_required
def upload_data():
    if current_user.role != 'administrator':
        return redirect(url_for('dashboard'))


    df = pd.DataFrame()
    
    if request.method == 'POST':
        csv_file = request.files.get("csv_file")
        xlsx_file = request.files.get("xlsx_file")
        json_file = request.files.get("json_file")
        parquet_file = request.files.get("parquet_file")
        txt_file = request.files.get("txt_file")

        if not any([csv_file, xlsx_file, json_file, parquet_file, txt_file]):
            return "Please upload at least one file."

        try:
        
            df_xlsx = pd.read_excel(xlsx_file) if xlsx_file else pd.DataFrame()
            df_csv = pd.read_csv(csv_file) if csv_file else pd.DataFrame()
            df_json = pd.read_json(json_file) if json_file else pd.DataFrame()
            df_txt = pd.read_csv(txt_file, delimiter="\t") if txt_file else pd.DataFrame()
            df_parquet = pd.read_parquet(parquet_file) if parquet_file else pd.DataFrame()

            df = pd.concat([df_csv, df_json, df_parquet, df_xlsx, df_txt], ignore_index=True)
            logging.info("Data loaded successfully.")
            
            process_and_upload_data(df)
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return "An error occurred while loading the data."
        
        return redirect(url_for('auth.dashboard'))
    
    return render_template('upload_data.html', df=df)




@auth.route('/view_data')
@login_required
def view_data():

    try:
        hospital_records = Hospital.query.all()
        if not hospital_records:
            return render_template('dashboard.html', error="No data available to display.")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return render_template('dashboard.html', error="Error fetching data.")


    data = {
        "Hospital Name": [record.hospitalname for record in hospital_records],
        "Hospital City": [record.hospitalcity for record in hospital_records],
        "Doctor Name": [record.doctorname for record in hospital_records],
        "Patient Name": [record.patientname for record in hospital_records],
        "Patient Gender": [record.patientgender for record in hospital_records],
        "Patient Age": [record.patientage for record in hospital_records],
        "Problem Diagnosed": [record.problem for record in hospital_records],
        "Patient Bill": [record.patientbill for record in hospital_records],
        "Patient State": [record.patientstate for record in hospital_records],
        "No of Days Admitted": [record.no_of_days for record in hospital_records],
        "Total Bill": [record.total_bil for record in hospital_records],
        "Age Group": [record.agegroup for record in hospital_records],
        "Cost per Day": [record.costperday for record in hospital_records],
    }
    df = pd.DataFrame(data)

    def create_plot(plot_func):
        buffer = BytesIO()
        plot_func()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        return img_base64

    plots = {}
    if current_user.role == 'administrator':
        plots['profit_plot'] = create_plot(lambda: sns.barplot(x="Hospital Name", y="Total Bill", data=df, estimator=sum, ci=None).set_title("Total Revenue by Hospital Name"))
        plots['cases_plot'] = create_plot(lambda: sns.countplot(x="Doctor Name", data=df).set_title("Number of Cases by Doctor Name"))
        plots['state_plot'] = create_plot(lambda: sns.countplot(x="Patient State", data=df).set_title("Number of Cases by Patient State"))
        plots['age_gender_plot'] = create_plot(lambda: sns.histplot(data=df, x="Patient Age", hue="Patient Gender", multiple="stack").set_title("Age Distribution by Gender"))
        plots['problem_gender_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Patient Gender", data=df).set_title("Cases by Problem Diagnosed and Gender"))
        plots['problem_age_group_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Age Group", data=df).set_title("Cases by Problem Diagnosed and Age Group"))
        plots['days_bill_plot'] = create_plot(lambda: sns.scatterplot(x="No of Days Admitted", y="Patient Bill", data=df).set_title("Patient Bill by Number of Days Admitted"))

    elif current_user.role == 'doctor':
        plots['cases_plot'] = create_plot(lambda: sns.countplot(x="Doctor Name", data=df).set_title("Number of Cases by Doctor Name"))
        plots['problem_gender_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Patient Gender", data=df).set_title("Cases by Problem Diagnosed and Gender"))
        plots['problem_age_group_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Age Group", data=df).set_title("Cases by Problem Diagnosed and Age Group"))

    elif current_user.role == 'patient':
        plots['problem_gender_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Patient Gender", data=df).set_title("Cases by Problem Diagnosed and Gender"))
        plots['problem_age_group_plot'] = create_plot(lambda: sns.countplot(x="Problem Diagnosed", hue="Age Group", data=df).set_title("Cases by Problem Diagnosed and Age Group"))

    
    return render_template('view_data.html', plots=plots, user_role=current_user.role)


@auth.route('/administrator')
@login_required
def admin():
    if not current_user.has_permission('administrator'):
        flash('Access denied.', 'danger')
        return redirect(url_for('auth.dashboard'))
    return "Admin Dashboard"

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('auth.login'))


@auth.route('/change_role/<int:user_id>', methods=['POST'])
def change_role(user_id):
    if not current_user.is_admin:
        flash('You do not have permission to change user roles.')
        return redirect(url_for('auth.manage_users'))

    user = User.query.get(user_id)
    if user:
        new_role = request.form.get('role') 
        user.role = new_role
        try:
            db.session.commit()
            flash(f"User role updated to {new_role} successfully.")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while updating the role. Please try again.")
            print(e)
    else:
        flash('User not found.')

    return redirect(url_for('auth.manage_users'))



@auth.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    else:
        flash('User not found!', 'danger')
    return redirect(url_for('auth.manage_users'))