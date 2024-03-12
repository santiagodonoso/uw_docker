from bottle import delete, get, template
import requests

##############################
@get("/")
def _():
    url = "http://host.docker.internal:8529/_api/cursor"
    q = {"query":"FOR user IN users RETURN user"}
    res = requests.post( url, json = q )
    res = res.json()
    print("#"*50)
    print(type(res))
    return template("index", users=res["result"])


##############################
@delete("/users/<key>")
def _(key):
    return f"""
    <template mix-target="#message" mix-after>
        <div>
            User delete with _key: {key}
        </div>
    <template>
    """


# Create the end-point for delete
# Connect to the db and delete the user with that id
# respond back to the browser with a mix <template>
# telling the browser to remove the user with that id






