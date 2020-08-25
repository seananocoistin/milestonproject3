import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

author = ""
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'acmebd'
app.config["MONGO_URI"] = 'mongodb+srv://stiurthoir:b1o2l3l4i5x6@cluster0-gaug0.mongodb.net/acmebd?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html",status=author)

@app.route("/about")
def about():
    return render_template("about.html",status=author)

@app.route("/signup")
def signup():
    return render_template("signup.html",status=author)

@app.route("/login")
def login():
    return render_template("login.html",status=author)

@app.route("/log_in", methods=["POST"])
def log_in():
    if request.method == "POST":
        if mongo.db.accounts.count_documents({"username":request.form["username"],"password":request.form["password"]})>0:
            global author
            author=request.form["username"]
            return create()
        else:
            return signup()

@app.route("/logout")
def logout():
    global author
    author = ""
    return index()

@app.route("/contact")
def contact():
    return render_template("contact.html",status=author)

@app.route("/listings")
def listings():
    return render_template("listings.html", tasks=mongo.db.users.find(),status=author)

@app.route("/mylisting")
def mylisting():
    return render_template("mylisting.html", tasks=mongo.db.users.find({"author":author}),status=author)

@app.route("/create")
def create():
    return render_template("create.html",status=author)

@app.route("/addlisting", methods=["POST"])
def addlisting():
    if request.method == "POST":
        newlisting = request.form.to_dict()
        newlisting.update({"author":author})
        mongo.db.users.insert(newlisting)
        return mylisting()

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        user=mongo.db.accounts.insert(request.form.to_dict())
        global author
        author=request.form["username"]
        return create()

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
