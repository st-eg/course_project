from flask import Flask
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Secret key
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:papa_dojo@localhost/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server
app.config['MYSQL_USER'] = 'root'  # MySQL login
app.config['MYSQL_PASSWORD'] = 'papa_dojo'  # MySQL password
app.config['MYSQL_DB'] = 'cars'  # Database name
app.config['UPLOAD_FOLDER'] = 'static/uploads' # Folder uploaded images, used to be displayed on the site
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
STATIC_URL = '/static/templates'
STATICFILES_DIRS = [
    '/static',  # Путь к папке static
]

# Initialize MySQL
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

mysql = MySQL()
mysql.init_app(app)