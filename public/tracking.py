from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import userCollection, trackedCollection
import datetime


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
