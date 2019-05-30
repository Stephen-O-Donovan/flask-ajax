#Script to initialise the app

from flask import Flask
from config import Config

# an app variable of type Flask
# __name__ is a python variable that refers to the
# name of the currently running file
main = Flask(__name__)

main.config.from_object(Config)

# app here refers to the package app
# routes is a python file containing 
# the links to the webpages
from app import routes 