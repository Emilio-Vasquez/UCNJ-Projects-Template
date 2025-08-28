"""
This is the run.py script

The purpose of this script is to serve as an entry point ot the Flask App

All it does:
    - import the Flask application function we created in the __init__.py (create_app)
    - Then it runs the app, with the debug mode on
"""

from app import create_app

## Creates the flask application instance
app = create_app()

## Now run the flask development server
if __name__ =="__main__":
    app.run(debug=True)