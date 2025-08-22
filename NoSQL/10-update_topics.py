#!/usr/bin/env python3
"""Module that changes all topics of a
school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Function matching school name to set their topics field."""
    """Modifies multiple documents in a collection"""
    """Returns the pymongo collection object"""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
