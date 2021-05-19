#!/usr/bin/env python3
"""HTTP route definitions"""

from flask import requests
from app import app

from app.database import (
    create,
    read,
    update,
    delete,
    scan
)

@app.route("/users", methods=["POST"]) # decorator
def create_user():                      # view functions
    user_data = request.json
    new_id = create (
        user_dta.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
        )
    return {
        "ok": True, 
        "message: "Success",
        "new_id": new_id
        }
