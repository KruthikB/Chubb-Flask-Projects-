import pandas as pd
from .models import db, Hospital
import logging

def process_and_upload_data(df):
    if df.empty:
        logging.warning("Empty DataFrame received; no data to upload.")
        return

    try:

        # Performing validations
        missing_data = df.isnull().sum()
        invalid_age = df[(df["Patient Age"] < 0) | (df["Patient Age"] > 120)]
        invalid_bill = df[df["Patient Bill"] <= 0]
        invalid_days_admitted = df[(df["No of Days Admitted"] < 1) | (df["No of Days Admitted"] > 365)]
        inconsistent_hospital_city = df.groupby("Hospital Name")["Hospital City"].nunique()
        inconsistent_hospital_city = inconsistent_hospital_city[inconsistent_hospital_city > 1]

        # Performing transformations
        df["Patient Bill"] = df["Patient Bill"].round(0).astype(int)
        df["Patient Gender"] = df["Patient Gender"].replace({"F": "Female", "M": "Male"})
        df["Total Bill"] = (df["Patient Bill"] * 1.10).round(0).astype(int)
        bins = [0, 12, 18, 35, 50, 65, 100]
        labels = ["Child", "Teen", "Young Adult", "Adult", "Middle Age", "Senior"]
        df["Age Group"] = pd.cut(df["Patient Age"], bins=bins, labels=labels)
        df["Cost per Day"] = (df["Patient Bill"] / df["No of Days Admitted"]).round(2)

        
        required_columns = [
            'Hospital Name', 'Hospital City', 'Doctor Name', 'Patient Name', 
            'Patient Gender', 'Patient Age', 'Problem Diagnosed', 'Patient Bill', 
            'Patient State', 'No of Days Admitted', 'Total Bill', 'Age Group', 'Cost per Day'
        ]

        for column in required_columns:
            if column not in df.columns:
                logging.error(f"Column missing: {column}")
                return

        for _, row in df.iterrows():
            try:
                hospital_record = Hospital(
                    hospitalname=row['Hospital Name'],
                    hospitalcity=row['Hospital City'],
                    doctorname=row['Doctor Name'],
                    patientname=row['Patient Name'],
                    patientgender=row['Patient Gender'],
                    patientage=row['Patient Age'],
                    problem=row['Problem Diagnosed'],
                    patientbill=row['Patient Bill'],
                    patientstate=row['Patient State'],
                    no_of_days=row['No of Days Admitted'],
                    total_bil=row['Total Bill'],
                    agegroup=row['Age Group'],
                    costperday=row['Cost per Day']
                )
                db.session.add(hospital_record)
                logging.info(f"Added record: {hospital_record}")
            except Exception as row_error:
                logging.error(f"Error adding record: {row_error}")
                continue 

        db.session.commit()
        logging.info("Data uploaded to the database successfully.")
    except Exception as e:
        logging.error(f"Error uploading data to the database: {e}")
        db.session.rollback()
