from app import create_app, db
from app.models import Pages

app = create_app()
app_context = app.app_context()
app_context.push()
db.create_all()