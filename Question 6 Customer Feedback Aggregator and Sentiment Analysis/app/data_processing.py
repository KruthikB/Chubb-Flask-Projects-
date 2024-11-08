import pandas as pd
from .models import db, Feedback
import logging

def process_and_upload_data(df):
    if df.empty:
        logging.warning("Empty DataFrame received; no data to upload.")
        return

    try:
        # Performing validations

        missing_data = df.isnull().sum()
        if missing_data.any():
            logging.warning(f"Columns with missing data: {missing_data[missing_data > 0].to_dict()}")
        
        invalid_date = df[pd.to_datetime(df["Date"], errors='coerce').isna()]
        if not invalid_date.empty:
            logging.warning(f"Invalid Date entries found: {len(invalid_date)}")

        invalid_source = df[~df["Source"].isin(["Social Media", "Survey", "Review Site"])]
        if not invalid_source.empty:
            logging.warning(f"Invalid Source entries found: {len(invalid_source)}")

        invalid_sentiment = df[~df["Sentiment Score"].isin(["Positive", "Neutral", "Negative"])]
        if not invalid_sentiment.empty:
            logging.warning(f"Invalid Sentiment Score entries found: {len(invalid_sentiment)}")

        if "Rating" in df.columns:
            invalid_rating = df[(df["Rating"] < 1) | (df["Rating"] > 5)]
            if not invalid_rating.empty:
                logging.warning(f"Invalid Rating entries found: {len(invalid_rating)}")

        # Performing transformations

        df["Feedback Length"] = df["Feedback Text"].apply(len)  # New column with feedback text length

        df["Date"] = pd.to_datetime(df["Date"], errors='coerce').dt.date  # Convert to Date format

        df["Sentiment Category"] = df["Sentiment Score"].map({"Positive": "Good", "Neutral": "Neutral", "Negative": "Bad"})  # Rename sentiment categories

        df["Feedback Text"] = df["Feedback Text"].str.capitalize()  # Capitalize feedback text

        df["Sentiment Numeric"] = df["Sentiment Score"].map({"Positive": 1, "Neutral": 0, "Negative": -1})  # Convert sentiment to numeric

        required_columns = [
            "Date", "Source", "Feedback Text", "Sentiment Score", 
            "Product/Service Category", "Rating", "Feedback Length",
            "Sentiment Category", "Sentiment Numeric"
        ]
        
        for column in required_columns:
            if column not in df.columns:
                logging.error(f"Column missing: {column}")
                return

        for _, row in df.iterrows():
            try:
                feedback_record = Feedback(
                    date=row['Date'],
                    source=row['Source'],
                    feedback_text=row['Feedback Text'],
                    sentiment_score=row['Sentiment Score'],
                    product_service_category=row['Product/Service Category'],
                    rating=row['Rating'],
                    feedback_length=row['Feedback Length'],
                    sentiment_category=row['Sentiment Category'],
                    sentiment_numeric=row['Sentiment Numeric']
                )
                db.session.add(feedback_record)
                logging.info(f"Added record: {feedback_record}")
            except Exception as row_error:
                logging.error(f"Error adding record: {row_error}")
                continue 

        db.session.commit()
        logging.info("Data uploaded to the database successfully.")
    except Exception as e:
        logging.error(f"Error uploading data to the database: {e}")
        db.session.rollback()
