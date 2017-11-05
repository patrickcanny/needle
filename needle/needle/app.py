import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from auth import playlist, songs, song_info, songs_in_list
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
# ############################
# #                   Functions
# ############################
def stripURI(fullURI):
    new = fullURI.replace('spotify:user:', '')
    return new

# ############################
# #                   Classes
# ############################
class UserForm(Form):
         username = StringField(u'Enter Spotify User To Roast:', validators = [validators.input_required()])

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

    if request.method == 'POST' and form.validate():
        session['username'] = stripURI(form.username.data)
        user = stripURI(form.username.data)
        PL = playlist(user)
        _playlists = PL.get_playlists()

        for _playlist in _playlists:
            playlist_name = _playlist.encode('utf-8')
            username = user
            cur = mysql.connection.cursor()

            var = cur.execute("SELECT * FROM Playlists WHERE playlist_name=%s;", [playlist_name])

            if var == 0:
                cur.execute("INSERT INTO Playlists(user_name, playlist_name) VALUES(%s, %s)", (username, playlist_name))
                mysql.connection.commit()
                cur.close()
            else:
                continue

        return redirect(url_for('playlists'))


    return render_template("main.html", form = form)

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

@app.route ("/upvote/<string:playlist_name>")
def upvote(playlist_name):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Playlists SET positive_votes = positive_votes+1 WHERE playlist_name = %s", [playlist_name])
    mysql.connection.commit()
    flash('Upvoted!', 'success')
    cur.close()
    return redirect(url_for('playlists'))

@app.route ("/downvote/<string:playlist_name>")
def downvote(playlist_name):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Playlists SET negative_votes = negative_votes+1 WHERE playlist_name = %s", [playlist_name])
    mysql.connection.commit()
    flash('Downvoted!', 'danger')
    cur.close()
    return redirect(url_for('playlists'))



@app.route("/view/<string:playlist_name>")
def viewsongs(playlist_name):
    cur = mysql.connection.cursor()

    #Cycle Through Songs
    un = session.get('username', None)
    SL = []
    SL[:] = []
    app.logger.info(SL)
    #TODO: Figure this Function Out...
    SL = songs_in_list(un)
    app.logger.info(SL)
    for song in SL:
        song_name = song.encode('utf-8')
        playlist = playlist_name
        app.logger.info(playlist)

        #Put all the stuff in DB
        # var = cur.execute("SELECT * FROM Songs WHERE playlist=%s;", [playlist_name])
        cur.execute("INSERT INTO Songs(song_name, playlist) VALUES(%s, %s)", (song_name, playlist))
        mysql.connection.commit()
    cur.close()


    # REQUERY To get all the songs again
    app.logger.info("about to requery...")
    cur = mysql.connection.cursor()
    app.logger.info(playlist_name)
    result = cur.execute("SELECT * FROM Songs WHERE playlist=%s;", [playlist_name])
    mysongs = cur.fetchall()
    cur.close()

    if result > 0:
        return render_template('view.html', songs = mysongs, playlistname = playlist_name)
    else:
        return redirect(url_for('index'))

@app.route ("/upvotesong/<string:song_name>")
def upvotesong(song_name):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Songs SET positive_votes = positive_votes+1 WHERE song_name = %s", [song_name])
    mysql.connection.commit()
    flash('Upvoted!', 'success')
    cur.close()
    return redirect(url_for('playlists'))

@app.route ("/downvotesong/<string:song_name>")
def downvotesong(song_name):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Songs SET positive_votes = negative_votes+1 WHERE song_name = %s", [song_name])
    mysql.connection.commit()
    flash('Downvoted!', 'danger')
    cur.close()
    return redirect(url_for('playlists'))



if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run()
