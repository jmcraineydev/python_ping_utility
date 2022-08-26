from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import userCollection, trackedCollection
import datetime
import requests
import re
import json
import asyncio


def getUserTrackedUrl():
    email = session.get("user")
    print(email)
    userUrls = trackedCollection.find({"email": email}, {})
    # print(list(userUrls))
    return list(userUrls)


def addUrlToTracking(url):
    now = datetime.datetime.now()
    email = session.get("user")
    print(email)
    trackedCollection.insert_one(
        {"url": url, "email": email, "status": "unknown", "date": now}
    )


def updateUserURLStatus(userUrls):
    print(userUrls)
    email = session.get("user")
    now = datetime.datetime.now()
    for url in userUrls:
        print(url["url"])
        query = {"url": url["url"]}
        newStatus = getUrlStatus(url)
        newValue = {"$set": {"status": newStatus, "date": now}}
        trackedCollection.update_many(query, newValue, upsert=False)


def updateAllURLStatus():
    now = datetime.datetime.now()
    allURLS = trackedCollection.find({})
    for url in allURLS:
        query = {"url": url["url"]}
        newStatus = getUrlStatus(url)
        newValue = {"$set": {"status": newStatus, "date": now}}
        trackedCollection.update_many(query, newValue, upsert=False)
    print("All URLS UPDATED")


def getUrlStatus(url):
    res = requests.get(url["url"], timeout=3)
    resData = res.status_code
    if resData >= 200:
        return "up"
    elif res >= 400:
        return "down"
    else:
        return "uknown"
