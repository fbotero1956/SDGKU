#!/usr/bin/env python3
"""Database operations"""

from flask import g     
import sqlite3

DATABASE = "user_db"
# open the db connection if not yet opened
def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# format output from tuple into a dictionary for display
def output_formatter(results: tuple):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = result [0]
        res_dict["first_name"] = result[1]
        res_dict["last_name"] = result[2]
        res_dict["hobbies"] = result[3]
        out.append(res_dict)
    return out 

# insert one row into the user table based on data passed
def create(first_name, last_name, hobbies):
    value_tuple = (first_name, last_name, hobbies)
    query = """
            insert into user (
                first_name,
                last_name,
                hobbies
                ) values (?,?,?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id

# get all rows from the user table
def read(id):
    id = (id,)
    cursor = get_db().execute("select * from user where id == (?)", (id))
    results = cursor.fetchone()
    cursor.close()
    return results

# update a row in the user table based on data passed and using the id to identify the row
def update(first_name, last_name, hobbies, id):
    value_tuple = (first_name, last_name, hobbies, id)
    query = """
            update user set
                first_name = (?),
                last_name = (?),
                hobbies = (?)
            where id == (?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id

# delete a row from the user table using the id as the identifier
def delete(id):
    value_tuple = (id,)
    query = """
            delete from user where id=(?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id

# get all rows from the user table
def scan():
    cursor = get_db().execute("select * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)