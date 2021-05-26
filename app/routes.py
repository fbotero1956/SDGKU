#!/usr/bin/env python3
"""HTTP route definitions"""

from flask import request
from app import app

from app.database import (
    create,
    read,
    update,
    delete,
    scan
)

# route to create new users
@app.route("/users", methods=["POST"]) # decorator
def create_user():                      # view functions
    user_data = request.json
    new_id = create (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
        )
    return {
        "ok": True, 
        "message": "Success",
        "new_id": new_id
        }


#route to get a single row from the user table
@app.route("/user")
def get_one_user():
    user_data = request.json
    user = read(
        user_data.get("id"),
        )
    return {
        "ok": True, 
        "message": "Successfull read",
       "users": user
        }
# route to update a row
@app.route("/users", methods=["PUT"]) # decorator
def update_user():                      # view functions
    user_data = request.json
    new_id = update (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("id")
        )
    return {
        "ok": True, 
        "message": "Successful update",
        "new_id": new_id
        }

# route to delete a row from user
@app.route("/delete", methods=["DELETE"]) # decorator
def delete_user():                      # view functions
    user_data = request.json
    new_id = delete (
        user_data.get("id"),
        )
    return {
        "ok": True, 
        "message": "Successfully deleted",
        "new_id": new_id
        }

#route to get all rows from the user table
@app.route("/users")
def get_all_user():
    users = scan()
    return {
        "ok": True, 
        "message": "Success",
       "users": users
        }

# misc routes for testing the app
@app.route('/user/<name>')
def user(name):
    return "<h1> hello %s!</h1>" % name

@app.route('/square/<int:number>')
def square(number):
    return ("<h1> %s squared is %s</h1>" % (number, number **2))

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your user agent is %s</p>" % user_agent