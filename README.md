# flask-webdev
flaskwebdevelopment2nd

## use pipenv to manage your project dependencies:
$ pipenv install

#### initiate virtual env 
$ pipenv shell

pipenv install <package name>
pipenv graph - to list installed packages

pipenv run pip freeze > requirements.txt
## install flask
pipenv install flask

## Initialization for a flask App
All Flask applications must create an application instance. create app.py

from flask import Flask
app = Flask(__name__)

$ flask run

## Development Web Server
Flask applications include a development web server that can be started with the flask run command.

(venv) $ export FLASK_APP=app.py
(venv) $ flask run

## Run dockerfile locally
build image with:
docker build -t IMAGE-NAME . 
~~docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE-NAME
docker run -p 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run" not this one maybe~~
docker run -p 5000:5000 -w /app -v "$(pwd):/app" IMAGE-NAME sh -c "flask run --host 0.0.0.0"
follow process:
docker container logs -f CONTAINER-ID
## Your first REST API endpoint
For now your db will be a python list.

from flask import Flask

app = Flask(__name__)

stores = [{"name": "Store Name", "items": [{"name": "Item Name", "price": 15.99}]}]


@app.get("/store") # endpoint decorator
def get_stores():
    return {"stores": stores}

#### get Insomia to make requests.
https://insomnia.rest/
all Insomnia files https://rest-apis-flask.teclado.com/insomnia-files/

#### create resources template to move enpoints to own files
create resources folder and create item.py and store.py
## create blueprint for each group of resources

resources/store.py
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores


blp = Blueprint("stores", __name__, description="Operations on stores")

The Blueprint arguments are the same as the Flask Blueprint1, with an added optional description keyword argument:

1. "stores" is the name of the blueprint. This will be shown in the documentation and is prepended to the endpoint names when you use url_for (we won't use it).
2. __name__ is the "import name".
3. The description will be shown in the documentation UI.

Now that we've got this, let's add our MethodViews. These are classes where each method maps to one endpoint. The interesting thing is that method names are important:

## Jinja control structures
chapter3 page28

## Localization of Dates and Times with Flask-Moment
https://momentjs.com/docs/#/displaying/ Moment.js documentation 

## JWT 
https://jwt.io/introduction

## docker image
docker build -t my-flask-site .
run the container
docker run -p 5000:5000 my-flask-site

## db migrations 
1. Make the necessary changes in the database models.
2. Generate a migration with the flask db migrate command.
3. Review the generated migration script and correct it if it has any inaccuracies.
4. Apply the changes to the database with the flask db upgrade command.

## How to set email to your console in Flask project
