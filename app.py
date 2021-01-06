from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/job_data"
db = SQLAlchemy(app)

# model :------------------------------------------------------------------
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    def __init__(self, mail, password):
        self.email = mail
        self.password = password

#db.create_all()

# controller :---------------------------------------------------------------
@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit']:
            mail = request.form['email']
            mdp = request.form['mdp']
            user = User(mail, mdp)
            db.session.add(user)
            db.session.commit()
            return render_template('home.html')
    else:
        return render_template('login.html')

# runing :-------------------------------------------------------------------
if __name__=='__main__':
    app.run(port=10, debug=True)
