from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose' #require for jwt
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = []



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000, debug=True)