#!/usr/bin/env python3
"""
This model inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Returns the new _id.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
