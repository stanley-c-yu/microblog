#The routes module contains URLs that the application implements
#	- in Flask, handlers for application routes are written as Python functions, called View Functions
#	- View Functions are mapped to one or more route URLs so that Flask knows what logic to execute 
#	  when a client requests a given URL.  

#Imports instance of Flask defined as "app" in __init__.py into routes.py
from flask import render_template
from app import app
#Import Login Form Class from forms.py
from app.forms import LoginForm

#The two @app.route lines of code are Python Decorators.  Decorators are used to modify functions that follow it.  
#	- In this case, the decorators create an association between the URLs '/' and '/index' and the following function.  
#	- Whenever a browser calls either of these two URLs, Flask will invoke the following function and pass the 
#	  return value of it back to the browser as a resonse.  
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In',form=form)
#The render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework. 
#Jinja2 substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided 
#in the render_template() call. Note that GitHub Pages doesn't support dynamic elements, so we'll have to axe 
#this when implementing a Flask web app on GH Pages. 
