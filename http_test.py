#!/usr/bin/env python3
"""help with the http requests"""

import requests
from pprint import pprint

# get and print all rows from user table, using the GET method
def scan():
    url= "http://127.0.0.1:5000/users"
    out = requests.get(url)

    pprint(out.json())



# add a user to the db, using the POST method
def create():
    url= "http://127.0.0.1:5000/users"
    test_data = {
        "first_name": "Felipe",
        "last_name" : "TestName13",
        "hobbies": "Horse Racing"
    }
    out = requests.post(url, json=test_data)
    try:

        pprint(out.json())
    except Exception:
        pprint(out.text)

# get and print a single record rows from user table, using the GET method
def read():
    url= "http://127.0.0.1:5000/user"
    test_data = {
        "id": "16",
    }
    out = requests.get(url, json=test_data)
    print("in the read function", out.text)
#  pprint(out.json())

#update a row in the user table, using PUT method
def update():
    url= "http://127.0.0.1:5000/users"
    test_data = {
        "first_name": "Sidney",
        "last_name" : "Botero", 
        "hobbies": "Gaming",
        "id": "16"
    }
    out = requests.put(url, json=test_data)
    try:

        pprint(out.json())
    except Exception:
        pprint(out.text)

# delete a row from the user table, using DELETE method
def delete():
    print("delete request2: ")
    url= "http://127.0.0.1:5000/delete"
    test_data = {
        "id": "13",
    }
    out = requests.delete(url, json=test_data)
    print("delete request3: ")


if __name__ == "__main__":
#    print("Scan request:")
#    scan()
     read()
#    print("Create request:")
#    create()
#    print("Delete request: ")
#    delete()
#    print("Update request:")
#    update()



