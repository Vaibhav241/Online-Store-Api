#G:\"Web Dev"\Api\"Section 5"\venv\Scripts\activate

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import ItemList,Item

app=Flask(__name__)
app.secret_key='vaibhav'
api= Api(app)
jwt=JWT(app,authenticate,identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,"/register")

if __name__ =="__main__":
    app.run(port=5000,debug=True)
