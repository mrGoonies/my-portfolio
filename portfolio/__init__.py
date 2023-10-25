from flask import Flask, render_template
from typing import List

app = Flask(__name__)
projects: List[str] = [
    {
        "name": "Micro Blog",
        "Description": 'The "Micro Blog" project is a simple yet powerful blogging platform that allows you to share your thoughts, ideas, and experiences in a quick and straightforward way. In this micro blog, anyone can post a message that will be displayed in the posts section, making it a dynamic space open to the creativity of the community. This project was developed using the Flask framework for application logic and MongoDB for data storage. ',
        "link": "https://microblog-54y3.onrender.com",
        # Acceder a un archivo estatico
        "image": "static/assets/projects/microblog.png",
    },
    {
        "name": "Daft Punk Tribute",
        "Description": 'The "Daft Punk Tribute" is a static website created as part of a web development boot camp, showcasing a tribute to the iconic electronic music duo, Daft Punk. This project was crafted using HTML, CSS, and SASS, serving as a testament to the skills and creativity developed during the web development journey.',
        "link": "https://mrgoonies.github.io/web-dev-coderhouse/",
        "image": "static/assets/projects/daft-punk.png",
    },
]


@app.get("/")
@app.get("/project")
def home():
    return render_template("home.html", projects=projects)


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    return render_template("contact.html")
