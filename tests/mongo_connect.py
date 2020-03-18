#!/usr/bin/env python3

from pymongo import MongoClient
from pprint import pprint


if __name__ == "__main__":
    # Need updated customer password
    client = MongoClient("mongodb+srv://customer:glcgQXd4prd1C3yk@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = client.admin

    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)

