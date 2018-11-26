from flask import render_template
from app import db
from app.main import BluePrint as bp
from app.models import Pages

@bp.route('/')
def index():
    pages = db.session.query(Pages).all()
    return render_template('index.html', pages=pages)

@bp.route('/page/<int:page_id>')
def view(page_id):
    page = db.session.query(Pages).filter_by(id=page_id).first()
    return render_template('page.html',id=page_id , title=page.title, content=page.content, timestamp=page.timestamp)