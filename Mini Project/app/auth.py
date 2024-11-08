from flask import render_template, redirect, url_for, flash, request,Blueprint
from app.models import User 
from app import db
from flask_login import current_user,login_required

auth = Blueprint('auth', __name__)

@auth.route('/manage_users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != 'administrator': 
        flash("Access denied.")
        return redirect(url_for('auth.dashboard'))

    users = User.query.all()
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        action = request.form.get('action')
        user = User.query.get(user_id)
        
        if action == 'delete' and user:
            db.session.delete(user)
            db.session.commit()
            flash(f"User {user.username} deleted successfully.")
        elif action == 'update_role' and user:
            new_role = request.form.get('role')
            if new_role:
                user.role = new_role
                db.session.commit()
                flash(f"Role updated to {new_role} for user {user.username}.")

        return redirect(url_for('auth.manage_users')) 

    return render_template('manage_users.html', users=users)