from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgress:jason@localhost/apitest'
db = SQLAlchemy(app)
@app.route("/")
def hello():
    return "Hello World!"