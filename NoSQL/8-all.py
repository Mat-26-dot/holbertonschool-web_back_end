#!/usr/bin/env python3
"""function that lists all documents in a collection"""

import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection """
    if not mongo_collection:
        return []
    """Return an empty list if no document in the collection"""
    return list(mongo_collection.find())