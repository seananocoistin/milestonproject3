<p align="center">
 
  <h2 align="center"><strong>ACME BUSINESS DIRECTORY</strong></h2>

  <p align="center">
    A BUSINESS DIRECTORY WITH USER CAPABILITY TO REGISTER TO A DATABASE
  </p>

## Welcome

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [User stories](#user-stories)
* [Motivation](#motivation)
* [Code Example](#code-example)
* [Roadmap](#roadmap)
* [Inspiration](#inspiration)
* [Author](#author)
* [Contact](#contact)

## About the project

The objective of this project is to create a Business Directory for **B2B** (*business to business*) and **B2C** (*business to consumer*) purposes. The purpose of this project is to demonstrate create, read, use, and delete functions on a website. The website would have functions and features for both B2B and B2C purposes but neither of them would contradict the other.

### Built with
The technologies that were used in the project were:
* [Gitpod](http://www.gitpod.io/) - used for the creation and designing of the website.
* [Github](http://www.github.com/) - used to host the project.
* [Bootstrap](https://getbootstrap.com/) - used to style and build the website.
* [HTML validator](https://validator.w3.org/) - used to valid the HTML code.
* [Heroku](https://www.heroku.com) - used to host the final site.
* [MongoDB](https://www.mongodb.com/) - used to create and host a database.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - used to help build the database. 
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/) - used the create wireframes.
* [CSS Gradient](https://cssgradient.io/) - used to select colours for the background.
* [Lightshot](https://app.prntscr.com/en/index.html) - used to make the screenshots of the site.

## Motivation
The reason why I chose to create a business directory is because it could serve as a directory for many activities. The data in this particular directory is for businesses but it could be used for all sorts of items such as recipes, books, people, music, etc.

## Code example

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

## User Stories
As a consumer, I want to a place to search for businesses and products. It should be easy to find products and services by entering a search term.
As a consumer, I want to be able to filter the entries so that I can find the best results based on the type of thing that I am searching for and where I am located.

As a business, I want to create an entry on a business directory to display my business to attract new clients. It should be easy and fast to create an account and be able to fill in the details of the businesses.
As a business, I want to be able to easily edit the account or, if need be, delete the account.

## User Experience
It should be easy to search for a product or a service in a search bar on the home page.
It should be easy to filter the entries by various criteria such as business type, location, business category, etc.
It should be easy to navigate around the website to move from entry to entry and to return to the home page.
The information in the entries should be clearly laid out and easy to read.

## Inspiration
I was inspired to make the business directory as I came across a business directory that was very clumsy and shoddy in the way that it was designed. I particularly like the [Manta business directory](http://www.manta.com).

## Testing
There was constant testing of the code during the design and construction of this website. Things frequently did not work and they had to be modified or sometimes changed entirely in order to get it to work. Html files were put through the HTML Validator to ensure that they were correct and error free.
The logging in and creation of new listings generated plenty of errors and those files had to be changed numerous times in order to get them to function as desired. That can be seen in the changes in the app.py and create.html, login.html, signup.html, edit.html files.  MondoDB had to consulted continuously to confirm that data entered into the website during registration and editing was received.
The layout and appearance underwent considerable change during the design. As more pages and funcions were added to the website, the appearance was found unsuitable so a new approach had to be undertaken. That is why the background image was removed and gradient colours were placed as a background.


## Future Development
The current website, as is stands, is to represent how a directory would function. The plan for future development is to add to the website and the directory so that it has more functions such being able to add photographs to the listings, being able to pay for a premium listing on the home page, more categories and filters so that users can search more to find their desired business. Users would be able to navigate the website better with buttons in order to move listings.

## Author
Seanán Ó Coistín

## Contact
www.seanan.info
Twitter: @seananocoistin
