import datetime
from app import db

class Pages(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(1000))
    content = db.Column(db.String(1000))
    timestamp = db.Column(db.String(1000))

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def commit_page(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return '<Page: id={}, title={},  content={}, timestamp={}>'.format(self.id,self.title,self.content, self.timestamp)
