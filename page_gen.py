import app
from app import Pages
from flask.ext.sqlalchemy import SQLAlchemy

class Page:

    def __init__(self, title, content):
        self.page = Pages(title=title,
                 content=content)
        self.db = SQLAlchemy(app)
        

def commit_page(self):
    page = Pages(title=title,
                 content=content)
    db.session.add(page)
    db.session.commit()