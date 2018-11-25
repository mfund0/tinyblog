import os, sys, mistune, datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Markup
from flaskext.markdown import Markdown

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
Markdown(app,  extensions=['codehilite'])
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pages.db') #+/pages.db' % os.getcwd()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pages(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(1000))
    content = db.Column(db.String(1000))
    timestamp = db.Column(db.String(1000))

    def __init__(self, title, content):
        print(basedir)
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def commit_page(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return '<Page: id={}, title={},  content={}, timestamp={}>'.format(self.id,self.title,self.content, self.timestamp)
    
@app.route('/')
def index():
    pages = db.session.query(Pages).all()
    return render_template('index.html', pages=pages)

@app.route('/page/<int:page_id>')
def view(page_id):
    page = db.session.query(Pages).filter_by(id=page_id).first()
    return render_template('page.html',id=page_id , title=page.title, content=page.content, timestamp=page.timestamp)


if __name__ == '__main__':
    app.run()