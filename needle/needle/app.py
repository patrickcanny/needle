import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = True

############################
#                   Functions
############################
def authorizeUser():
    #Spotify Authentication Stuff Goes Here

############################
#                   Routes
############################
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/main")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
