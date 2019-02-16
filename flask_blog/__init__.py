from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "2fc3a42f0dd842ba075ef34e5f1679bb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # this(/// - three forward slashes  ) will set relative apth to DB
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'#function name of route #: The name of the view to redirect to when the user needs to log in.
login_manager.login_message_category = 'info' #  The message category to flash when a user is redirected to the login                             

from flask_blog import routes # this called after app brcause for routes it need apps to be initialized