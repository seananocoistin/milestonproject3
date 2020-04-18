<p align="center">
 
  <h2 align="center"><strong>ACME BUSINESS DIRECTORY</strong></h2>

  <p align="center">
    A MOCK-UP OF A BUSINESS DIRECTORY WITH USER CAPABILITY TO REGISTER TO A DATABASE
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

The objective of this project is to create a Business Directory for **B2B** (*business to business*) and **B2C** (*business to consumer*) purposes. The purpose of this project is to demonstrate create, read, use, and delete functions on a website. That happens here.

### Built with
The technologies that were used in the project were:
* [Gitpod](http://www.gitpod.io/)
* [Bootstrap](https://getbootstrap.com/)
* [Verifiers]()
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [HTML validator](https://validator.w3.org/)
* [Heroku](https://www.heroku.com)
* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/)

## User Stories
A business using the website could add register their business with the directory and insert a listing so that potential customers and clients can find their business.

A consumer using the website could search the directory in order to find a product or a service.

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

## Roadmap
Not all of the proposed features of the business directory are included in this model e.g there is no directory to search through, there are no business categories, the search function does not function etc. It is not necessary to include them at present as they are not entirely needed in order to demonstrate the purpose of this directory. For example, many categories could be added but it would take a lot of time to do so.

## Inspiration
I was inspired to make the business directory as I came across a business directory that was very clumsy and shoddy in the way that it was designed. I particularly like the [Manta business directory](http://www.manta.com). While it would be nice to emulate such a directory, time constraints did not allow but it will continue to serve as an inspiration and guide as to what can be achieved.

## Author
Seanán Ó Coistín

## Contact
www.seanan.info
Twitter: @seananocoistin
