from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    ROLES = {
        'administrator': ['admin', 'analyst', 'viewer'],
        'doctor': ['analyst', 'viewer'],
        'patient': ['viewer'],
    }
    
    def has_permission(self, required_role):
        return required_role in self.ROLES.get(self.role, [])

    @property
    def is_admin(self):
        return self.role == 'administrator'
    

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    hospitalname = db.Column(db.String(50), nullable=False)
    hospitalcity = db.Column(db.String(50), nullable=False)
    doctorname = db.Column(db.String(50), nullable=False)
    patientname = db.Column(db.String(50), nullable=False)
    patientgender = db.Column(db.String(10), nullable=False)
    patientage = db.Column(db.Integer, nullable=False)
    problem = db.Column(db.String(50), nullable=False)
    patientbill = db.Column(db.Integer, nullable=False)
    patientstate = db.Column(db.String(50), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    total_bil = db.Column(db.Integer, nullable=False)
    agegroup = db.Column(db.String(20), nullable=False)  
    costperday = db.Column(db.Numeric(10, 2), nullable=False) 

