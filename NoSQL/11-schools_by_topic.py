#!/usr/bin/env python3
"""returns the list of school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the given topic.

    Args:
        mongo_collection: pymongo collection object
        topic: string representing the topic to search for

    Returns:
        List of school documents (dict) matching the topic
    """
    result = mongo_collection.find({"topics": topic})

    return result
