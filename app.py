import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'acmebd'
app.config["MONGO_URI"] = 'mongodb+srv://stiurthoir:b1o2l3l4i5x6@cluster0-gaug0.mongodb.net/acmeBD?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
