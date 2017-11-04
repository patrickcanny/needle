import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import auth
from wtforms import Form, StringField, validators


app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = True

############################
#                   Classes
############################
class UserForm(Form):
    username = StringField(u'Enter Spotify User To Roast:', validators = [validators.input_required()])

############################
#                   Functions
############################

############################
#                   Routes
############################
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/main", methods = ['GET','POST'])
def main():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.username.data

    return render_template("main.html", form= form)

@app.route("/playlists", methods = ['GET','POST'])
def playlists():
    if request.method == 'GET' and form.validate():
        user = form.username.data
        playlists = playlist(user)
    return

if __name__ == "__main__":
    app.run()
