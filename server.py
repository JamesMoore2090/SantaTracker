# imports
import os
#import MySQLdb
from flask import Flask, render_template, request, session

################################################################################
#setting up the flask app

app = Flask(__name__)


app.secret_key = os.urandom(24).encode('hex')


    
    
################################################################################
# database stuff!

# def connectToDB():
#   try:
#     return MySQLdb.connect("localhost", "jmoore7", "" , "bioseeddb")
#   except:
#     print("Can't connect to database")
    
################################################################################
# home page

@app.route('/')
def mainIndex():
    #return "Hello World!"
    return render_template('index.html')

################################################################################
# about page

@app.route('/about')
def about():
    #return "Hello World!"
    return render_template('about.html')

################################################################################
# blog page

@app.route('/blog')
def blog():
    #return "Hello World!"
    return render_template('blog.html')

################################################################################

# contact page

@app.route('/santaLocation')
def santaLocation():
    #return "Hello World!"
    return render_template('santaLocation.html')


################################################################################

# admin page

@app.route('/admin')
def admin():
    #return "Hello World!"
    return render_template('admin.html')
    
################################################################################

# admin login form

@app.route('/adminLogin', methods = ['POST', 'GET'])
def adminLogin():
    username = request.form['username']
    password = request.form['password']
    if username == 'bear567' and password == 'Turtle789!':
        session['username'] = 'admin'
        #return "Hello World!"
        return render_template('adminPage.html')
    return render_template('index.html')
    
################################################################################

# Write Blog

@app.route('/writeBlog')
def writeBlog():

    return render_template('writeBlog.html')
    
################################################################################

# Write Blog

@app.route('/startTracker')
def startTracker():

    return render_template('startTracker.html')
    
################################################################################

# write about santa's Status

@app.route('/santaStatus')
def santaStatus():

    return render_template('santaStatus.html')
    
################################################################################

# write Map

@app.route('/map')
def map():

    return render_template('map.html')
    
################################################################################

# logout

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')
    
################################################################################
# this has to be at the end

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
    
################################################################################