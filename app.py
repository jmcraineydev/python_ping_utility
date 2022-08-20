import requests
from dotenv import load_dotenv
import os

load_dotenv()


def makeRequest():
    res = requests.get(os.getenv("HOST"))
    # response = json.loads(res.text)
    return res


print(makeRequest())
