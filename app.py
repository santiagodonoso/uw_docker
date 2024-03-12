from bottle import get
import requests


@get("/")
def _():
    url = "http://host.docker.internal:8529/_api/cursor"
    q = {"query":"FOR user IN users RETURN user"}
    res = requests.post( url, json = q )
    return res








