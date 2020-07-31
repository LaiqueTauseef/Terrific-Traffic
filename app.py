from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from functools import wraps
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from tabledef import *
import time
app = Flask(__name__, static_folder='static')

app.secret_key = "anonymous"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():

    return render_template("login.html")


@app.route('/choose', methods=['GET', 'POST'])
def choose():
	if request.method == 'POST':
		return render_template("choose.html")
		
	if request.method == 'GET':
		return render_template("choose.html")


# Route for handling the login page logic   
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_(
            [POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()

        if result:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('choose'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return render_template("login.html")



	
@app.route('/play', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['filename']
		#f.save(f.filename)
		name = f.filename 
		os.system('cd C:/Users/ABC/Desktop/flask && python yolo_video.py --input videos/' + name + ' --output static/' + name + ' --yolo yolo')
		time.sleep(1)
		return render_template('play.html')
    

	
	
@app.route('/help')
def help():
	return render_template('help.html')


	
	
# start the server with the 'run()' method
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
