# import fast api
from fastapi import FastAPI

# create an instance of fast api
app = FastAPI()

# create a route
@app.get("/{first_name}/{last_name}")
def index(first_name, last_name):
    return {"first_name": first_name, "last_name": last_name, "full_name": "{} {} {}".format(first_name, last_name, "is great")}