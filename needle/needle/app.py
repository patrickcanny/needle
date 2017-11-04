import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import auth
from wtforms import Form, StringField, validators


app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = True

############################
#                   Functions
############################
#def authorizeUser():
    #Spotify Authentication Stuff Goes Here

############################
#                   Routes
############################
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/main", methods = ['GET','POST'])
def main():
    return render_template("main.html")

@app.route("/playlists", methods = ['GET','POST'])
def playlists():
    if request.method == 'GET' and form.validate():
        user = form.username.data
        playlists = playlist(user)
    return

if __name__ == "__main__":
    app.run()
