import os
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

Bootstrap(app)
Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", message="Not Found"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", message="Server Error"), 500


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"))


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


class NameForm(FlaskForm):
    name = StringField("What is you name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
