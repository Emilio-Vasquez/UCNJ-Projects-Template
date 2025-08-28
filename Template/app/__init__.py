"""
This is the __init__.py script

It acts as the glue for the entire flask application

It essentially formats the app/ folder as a package, making our scripts into moduels
Giving us the ability to basically import scripts

It also loads the configurations from the config file, and it initalizes extensions, as well as
registering blueprints (routes) into the application
"""

from flask import Flask ## This class "Flask" let's us create an instance of Flask
from .db import init_app ## This is the function that closes our db connection automatically
from .routes import main ## We'll create this file later, with reports
## and we'll import blue print here
## And we do that to register routes into our application

def create_app():
    """
    Will be to have it run on our "run.py" to create the app and it running on a development server
    """

    app = Flask(__name__, template_folder="templates", static_folder ="static")
    ## The double underscore 'name' is a built-in variable to get the name of the current file
    ## and we're trying to register the template folder and the static folder into our flask app

    app.config.from_object("config.Config")

    init_app(app)

    app.register_blueprint(main)

    return app
