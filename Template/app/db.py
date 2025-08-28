"""
This is the db.py script

This script will be responsible for connecting to your MySQL database and cleaning it up properly

1st: It's because it gives us a centralized connection logic
2nd: Whenever we want to use the db, we can call this script to connect to our database
3rd: We'll properly open and properly close the database connection
"""

import mysql.connector ## This is the driver for MySQL, it's important to connect with Python
from flask import current_app, g ## current_app gives us the configurations we need from the config.py script
## And the g bascially stores the per-request data that we get back from the config call

def get_db():
    """
    The purpose of this function 'get_db()' is to open up the sql connection and send it to your python location

    - the 'g' is a special flask object that exists only for one request
    - First we have to call in a request, then store it in the g object as g.db
    - Then for later calls, we just reuse the g.db object
    - At the end of the call, we close the connection using the close_db() that we'll create later
    """

    if "db" not in g:
        g.db = mysql.connector.connect(
            host = current_app.config["DB_HOST"],
            port = current_app.config["DB_PORT"],
            user = current_app.config["DB_USER"],
            password = current_app.config["DB_PASSWORD"],
            database = current_app.config["DB_NAME"]
        )
    
    return g.db

def close_db(e=None):
    """
    This function closes the database connection at the end of a request
    
    This is because Flask calls it automatically, because we'll initialize as such in our init_app() function that
    We'll also create in a bit
    """
    db = g.pop("db", None) ## Removes "db" from g if it does exist
    if db is not None:
        db.close()

def init_app(app):
    """
    This is called from the __init__.py script, once the flask app isntance is created

    This registers close_db(), so every request automatically closes the DB connection after
    """
    app.teardown_appcontext(close_db) ## calling the close_db() function

## Now let's create a query_test() function just to test our connection
def query_test(sql, params=()):
    """
    Run a SELECT query for testing purposes

    - If it returns true then the query executes succesfully and it's working
    - If it returns False no rows are found or it's false
    - If there's an error, that means there was probably a sql connection that was bad
    """

    conn = get_db()
    with conn.cursor(dictionary=True) as cur:
        cur.execute(sql, params)
        row = cur.fetchone()
        return True if row else False