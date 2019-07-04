import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, verbose=True)

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

config = {"dev": DevConfig,"docker": DockerConfig}
