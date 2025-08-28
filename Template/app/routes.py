"""
This routes.py script will contain the routes/path for our application
"""

from flask import Blueprint, render_template, request, session, url_for
from .db import query_test
from .login import handle_login
from .register import handle_registration

main = Blueprint("main", __name__)
## initializies a blueprint

@main.route("/")
def index():
    ## We will change this to render html home page later on

    # ok = query_test("SELECT 1")
    # if ok:
    #     return "<h1>Flask is running! Database Connection is Successful!</h1>"
    # else:
    #     return "<h1>Flask is running! BUT Database test query returned no results! :c </h1>"
    return render_template("index.html")

## Add the route for the login
@main.route("/login", methods=["GET", "POST"]) ## localhost/login
def login():
    if request.method == "POST":
        ## Login.py script logic here
        print("hi!") ## erase this because it's just there to prevent error
    
    return render_template("login.html")

## Adding the register route
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ## Call the register.py script logic here
        print("Hi!") ## erase this
    
    return render_template("register.html")

## Adding the about page route
@main.route("/about")
def about():
    return render_template("about.html")