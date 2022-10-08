import collections
from itertools import product
from pydoc import doc
from typing import Collection
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
#password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://tanveerisonline:Realme%4010a@cluster0.vtsyekv.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
# print(dbs)
test_db = client.db_test
collections = test_db.list_collection_names()
print(collections)

##............................##
## CREATING AND INSERTING SINGLE DATA ENTRY##
##............................##


def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Tanveer",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

# insert_test_doc()    ## Calling function here


##..........................................................##
    ## CREATING AND INSERTING DATA MULTIPLE DATA ENTRIES##
##..........................................................##

# Creating a new data base using Editor
production = client.production  # Creating a new DB here
# creating a new collection inside production db
person_collection = production.person_collection


def create_documents():  # Inserting document using a function
    first_name = ["Abrahim", "barbara", "connor", "danny",
                  "eathen"]  # inserted data in first_name column
    last_name = ["Lincoln", "Ross", "Rhynes", "Hopkins",
                 "Hunt"]  # inserted data in last_name column
    ages = [82, 36, 42, 65, 51]  # inserted data in ages column

    docs = []

    # inserting data using ## FOR LOOP ##
    for first_name, last_name, age in zip(first_name, last_name, ages):
        doc = {"first_name": first_name, "last_name": last_name, "ages": age}
        docs.append(doc)  # putting doc data into docs[] empty array

    # person_collection.insert_many(docs)
    # here we are inserting the data into the collection
    person_collection.insert_many(docs)


# create_documents()  # // calling function here


##..........................................................##
    ## READING INSERTED DATA DATA ENTRIES##
##..........................................................##
printer = pprint.PrettyPrinter()   # // importing pretty printer


def find_all_people():  # defining a function to read data
    people = person_collection.find()

    for person in people:
        printer.pprint(person)


# find_all_people() # // calling function here


##..........................................................##
## READING OR FINDING A SPECIFIC VALUE FROM THE DOCUMENT ##
##..........................................................##

def find_specific_item():
    item = person_collection.find_one({"first_name": "Abrahim"})
    printer.pprint(item)


# find_specific_item() # // calling function here


##..........................................................##
##   FINDING NUMBER OF OBJECTS IN THE DOCUMENT ##
##..........................................................##

def count_all_people():
    count = person_collection.count_documents(filter={})
    print("Number of people", count)


# count_all_people() # // calling function here


##..........................................................##
##   FINDING BY ID FROM THE DOCUMENT ##
##..........................................................##

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    print(person)


get_person_by_id("633d7eda308dd36d879de4bd")


##..........................................................##
##   FINDING BY ID FROM THE DOCUMENT ##
##..........................................................##
