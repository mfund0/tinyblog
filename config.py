import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'),verbose=True)

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pages.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    pass

class DockerConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            "DATABASE_URL"
        )
    
    "mysql+pymysql://blog:<database-password>@dbserver/pages"

config = {"dev": DevConfig,"docker": DockerConfig}