from app.app import create_app
from app.extensions.database import db

app = create_app()
app.app_context().push()

db.session.commit()