from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flaskext.markdown import Markdown
from config import Config


#Create an insatnce of db that is not attached to an app
db = SQLAlchemy()

def create_app(config_class=Config):
    '''Application factory function'''
    
    app = Flask(__name__)
    Markdown(app,  extensions=['codehilite'])
    app.config.from_object(Config)
    db.init_app(app)

    from app.main import BluePrint as main_bp
    app.register_blueprint(main_bp)
    
    return app


from app import models