import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "acmeBD"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a recor by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def add_record():
    print("")
    about = input("Enter name of the business")
    contact = input("Enter contact details")
    services = input("Enter the type of service provided")
    hours = input("Enter business hours")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
