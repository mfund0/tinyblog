from flask import Blueprint

BluePrint = Blueprint('main', __name__)

from app.main import routes
