from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "2fc3a42f0dd842ba075ef34e5f1679bb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # this(/// - three forward slashes  ) will set relative apth to DB
db = SQLAlchemy(app)

from flask_blog import routes # this called after app brcause for routes it need apps to be initialized