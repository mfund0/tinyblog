import unittest
from config import Config
from app import db, create_app
from app.models import Pages

class TestConfig(Config):
    '''Test configuration'''

    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class PageModel(unittest.TestCase):
    ''' Test PageModel ops '''
    def test_create_all(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()