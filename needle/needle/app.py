import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, validators

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = True

@app.route("/"):
def login:
    return render_template("views/login.html")
