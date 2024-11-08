
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  
from config import Config


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  

login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    
    from .routes import auth
    app.register_blueprint(auth)

    from .models import User
    with app.app_context():
        db.create_all() 

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
