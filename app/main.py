from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")