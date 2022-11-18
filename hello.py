from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", message="Not Found"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", message="Server Error"), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
