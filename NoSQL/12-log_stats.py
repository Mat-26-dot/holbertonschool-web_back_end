#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


"""Connect to MongoDB running on localhost"""
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

"""Count total number of documents in the collection"""
count = collection.count_documents({})

"""List of HTTP methods to count"""
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

"""Count documents for each HTTP method"""
method_counts = {method: collection.count_documents
                ({"method": method}) for method in methods}

"""Count documents where method is GET and path is /status"""
get_status_count = collection.count_documents({"method": "GET",
                                            "path": "/status"})

"""Print results in requested format"""
print(f"{count} logs")
print("Methods:")
for method in methods:
    print(f"\method={method} count={method_counts[method]}")
print(f"{get_status_count} logs where method=GET and path=/status")