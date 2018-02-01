from app import app
from flaskext.mysql import MySQL

database = MySQL()
app.config['MYSQL_DATABASE_HOST']       = 'localhost'
app.config['MYSQL_DATABASE_USER']       = 'root'
app.config['MYSQL_DATABASE_PASSWORD']   = ''
app.config['MYSQL_DATABASE_DB']         = 'test'
database.init_app(app)
