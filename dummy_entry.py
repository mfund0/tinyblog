from app import create_app
from app.models import Pages

app = create_app()
app.app_context().push()

content = open('content.md','r')

p = Pages("From Docker",content.read())
p.commit_page()
