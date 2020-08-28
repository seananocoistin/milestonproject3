import os
import json
import smtplib, ssl
import base64
from bson.binary import Binary
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
    return render_template("listings.html", tasks=mongo.db.listings.find(),status=author)

@app.route("/mylisting")
def mylisting():
    return render_template("mylisting.html", tasks=mongo.db.listings.find({"author":author}),status=author)

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
            password = "123456"
            """message = "Your password is: "+ user["password"]"""

            """context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)"""
            return render_template("forgot.html",send=True,email=receiver_email)

@app.route("/create")
def create():
    return render_template("create.html",status=author)

@app.route("/edit", methods=["POST"])
def edit():
    if request.method == "POST":
        listingtoedit = request.form.to_dict()
        return render_template("edit.html",status=author,data=listingtoedit)


@app.route("/addlisting", methods=["POST","GET"])
def addlisting():
    if request.method == "POST":
        newlisting = request.form.to_dict()
        """image_file = open(request.files["image"], "r").read()
        encoded_string = base64.b64encode(image_file).decode()"""
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
