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
* [Gitpod](http://www.gitpod.io/)
* [Bootstrap](https://getbootstrap.com/)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [HTML validator](https://validator.w3.org/)
* [Heroku](https://www.heroku.com)
* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/)

## Motivation
The reason why I chose to create a business directory is because it could serve as a directory for many activities. The data in this particular directory is for businesses but it could be used for all sorts of items such as recipes, books, people, music, etc.

## Code example

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

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

## Author
Seanán Ó Coistín

## Contact
www.seanan.info
Twitter: @seananocoistin