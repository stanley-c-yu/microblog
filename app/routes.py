#The routes module contains URLs that the application implements
#	- in Flask, handlers for application routes are written as Python functions, called View Functions
#	- View Functions are mapped to one or more route URLs so that Flask knows what logic to execute 
#	  when a client requests a given URL.  

#Imports app module
from app import app

#The two @app.route lines of code are Python Decorators.  Decorators are used to modify functions that follow it.  
#	- In this case, the decorators create an association between the URLs '/' and '/index' and the following function.  
#	- Whenever a browser calls either of these two URLs, Flask will invoke the following function and pass the 
#	  return value of it back to the browser as a resonse.  
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"