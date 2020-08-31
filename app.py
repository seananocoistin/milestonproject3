import os
import json
import smtplib, ssl
import base64
import datetime
if os.path.exists("env.py"):
  import env
from bson.binary import Binary
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


author = ""
app = Flask(__name__)
app.config["MONGO_URI"]= os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%H")
    today = datetime.datetime.now().strftime("%w")
    return render_template("index.html",tasks=mongo.db.listings.find(),status=author,today=int(today),int=float,now=int(now))

@app.route("/search", methods=["POST"])
def search():
    now = datetime.datetime.now().strftime("%H")
    today = datetime.datetime.now().strftime("%w")
    if request.method == "POST":
        listings = mongo.db.listings.find({"business_name": { '$regex': ".*"+request.form["search"] +".*", '$options' : 'i'} })
        return render_template("listings.html",tasks=listings,status=author,today=int(today),int=float,now=int(now))

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
        if mongo.db.accounts.find({"username":request.form["username"],"password":request.form["password"]}).count()>0:
            global author
            author=request.form["username"]
            return mylisting()
        else:
            return render_template("login.html",loginattempt=True)

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
    now = datetime.datetime.now().strftime("%H")
    today = datetime.datetime.now().strftime("%w")
    return render_template("listings.html", tasks=mongo.db.listings.find(),status=author,today=int(today),int=float,now=int(now))

@app.route("/mylisting")
def mylisting():
    now = datetime.datetime.now().strftime("%H")
    today = datetime.datetime.now().strftime("%w")
    return render_template("mylisting.html", tasks=mongo.db.listings.find({"author":author}),status=author,today=int(today),int=float,now=int(now))

@app.route("/deletelisting", methods=["POST"])
def deletelisting():
    if request.method == "POST":
        mongo.db.listings.remove({"business_name":request.form["business_name"]},{"justOne":True})
        
        return render_template("mylisting.html", tasks=mongo.db.listings.find({"author":author}),status=author)

@app.route("/forgot")
def forgot():
    return render_template("forgot.html")

@app.route("/forgotemail", methods=["POST"])
def forgotemail():
    if request.method == "POST":
        user = mongo.db.accounts.find({"email":request.form["email"]})
        if user.count()>0:
            port = 465 # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "info@gmail.com" # Enter your address
            receiver_email = request.form["email"]
            password = ""
            return render_template("forgot.html",send=True,email=receiver_email)

@app.route("/create")
def create():
    return render_template("create.html",status=author)

@app.route("/edit", methods=["POST"])
def edit():
    if request.method == "POST":
        listingtoedit = request.form.to_dict()
        return render_template("edit.html",status=author,data=listingtoedit,int=float)


@app.route("/addlisting", methods=["POST","GET"])
def addlisting():
    if request.method == "POST":
        newlisting = request.form.to_dict()
        newlisting.update({"author":author})
        mongo.db.listings.insert(newlisting)
        return mylisting()

@app.route("/editlisting", methods=["POST"])
def editlisting():
    if request.method == "POST":
        newlisting = request.form.to_dict()
        newlisting.update({"author":author})
        mongo.db.listings.update_one({"author":author,"business_name":newlisting["business_name"]},{"$set":newlisting})
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
