from flask import session
from . import trackedCollection
import datetime
import requests
from requests.exceptions import Timeout


def getUserTrackedUrl():
    email = session.get("user")
    userUrls = trackedCollection.find({"email": email}, {})
    return list(userUrls)


def addUrlToTracking(url):
    now = datetime.datetime.now()
    email = session.get("user")
    trackedCollection.insert_one(
        {"url": url, "email": email, "status": "unknown", "date": now}
    )


def updateUserURLStatus(userUrls):
    now = datetime.datetime.now()
    for url in userUrls:
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
    try:
        res = requests.get(url["url"], timeout=3)
        resData = res.status_code
    except Timeout:
        print("URL request timed out - status changed to down")
        resData = 400
    except requests.exceptions.ConnectionError:
        print("URL Connection Error status changed to down")
        resData = 400
    if resData >= 400:
        return "❌"
    elif resData >= 300:
        return "🔀"
    if resData >= 200:
        return "✅"
    else:
        return "🤷‍♂️"
