from Fakeprinterst import database, app
from Fakeprinterst.models import Usuario, Foto

with app.app_context():
    database.create_all()

