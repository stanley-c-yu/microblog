#Imports Flask
from flask import Flask

# Creates an instance of Flask
#	- __name__ is a Python pre-defined variable set to the name of the module in which it's used.
#	- Flask uses the location of the module passed here as a starting point for when it needs to 
#	  load all associated resources, such as template files
app = Flask(__name__)

#Imports the routes module
from app import routes