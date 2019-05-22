import sqlite3
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

class Item(Resource):
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price':row[1]}}
        return {'message':'Item not found'}, 404



    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float,
        required=True,
        help="This field cannot be left blank!")
        # data = request.get_json()
        data = parser.parse_args()
        item = next(filter(lambda x:x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        retJson = []
        for row in result:
            temp = {'name': row[0], 'price': row[1]}
            retJson.append(temp)
        connection.close()
        return retJson
