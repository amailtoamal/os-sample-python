from flask import Flask, redirect, url_for, request, json
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://amal:amal1234@ds131743.mlab.com:31743/final_whistle"
mongo = PyMongo(app)


@app.route('/login', methods=['POST'])
def login():
      x = mongo.db.users.find()
      return dumps(x)


if __name__ == '__main__':
   app.run()
