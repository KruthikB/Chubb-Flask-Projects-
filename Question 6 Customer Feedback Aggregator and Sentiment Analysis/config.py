import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

    #Database for SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///customer_feedback.db'

    #Database for Postgres
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kruthik1207@localhost:5432/users'
    
    #Database for MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kruth!k1207@localhost/customerfeedback'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
