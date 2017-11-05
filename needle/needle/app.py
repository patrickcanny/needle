import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from auth import playlist, songs, song_info
from wtforms import Form, StringField, validators
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = True

#CONFIG MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'NEWPASSWORD'
app.config['MYSQL_DB'] = 'needle'
app.config['MYSQL_CURSOR'] = 'DictCursor'

mysql = MySQL(app)

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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/main", methods = ['GET','POST'])
def main():
    form = UserForm(request.form)
    session['username'] = form.username.data

    if request.method == 'POST' and form.validate():
        user = form.username.data
        PL = playlist(user)
        _playlists = PL.get_playlists()
        for _playlist in _playlists:
            playlist_name = _playlist
            username = user
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Playlists(user_name, playlist_name) VALUES(%s, %s)", (username, playlist_name))
            mysql.connection.commit()
            cur.close()

        flash('Added!', 'success')
        return redirect(url_for('playlists'))
    return render_template('main.html', form = form)

@app.route("/playlists", methods = ['GET','POST'])
def playlists():
    cur = mysql.connection.cursor()
    username = session.get('username', None)
    result = cur.execute("SELECT * FROM Playlists WHERE user_name=%s;", [username])
    playlists = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template("playlists.html", playlists=playlists)
    else:
        msg = "No Playlists Found!"
        return render_template("playlists.html", msg=msg)


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run()
