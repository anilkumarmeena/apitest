from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jason@localhost/apitest'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    def __init(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    myuser = User.query.all()
    return render_template('main.html', myuser=myuser)

@app.route("/post_user", methods=['POST'])
def post_user():
    user = User(username=request.form['username'], email=request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('hello'))