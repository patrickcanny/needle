# needle
It's like Rotten Tomatoes, except for Spotify.

# About
Needle is a web application that allows users to rate their friends' playlists. After obtaining the URI from a Spotify Profile,
any Spotify user can be searched. A list of their public playlists will be generated, along with a favorability
rating for each. The user can then vote on the playlists, or even individual songs in that playlist. Sessions are isolated,
but end as soon as another user is searched for. All data is stored in a local MYSQL database, making this app unfit for
general release in its current state.

Needle was created with the Flask Microframework for Python, with Bootstrap views. We also utilized the Spotipy API client
for Python in order to interface with the Spotify API. We utilized WTForms for form validation and generation, along with a
MySQL database to store information. All referenced technology can be found in *References* below.

We had originally intended to develop Needle as a mobile application, but ran into numerous issues developing with the iOS SDK
for Spotify. We would like to port this app to a mobile platform in the future, and possibly add live-time modification of playlists in order
to make the app mor similar to Tinder.

Overall, we consider this project to be a success. This was the first Hackathon for 2/3 of our team, and one of our members' first time writing
significant code. We were able to effectively delegate the workload and take personal responsibility for a major facet of the app's success. Though
the app does have a number of bugs, we're proud of the work we put in to developing a clean and interesting platform, and feel that our idea
is wonderful.

# Installation
- Requirements
  - Python (2.7.11 or later)
  - Flask (0.12.2)
  - Virtualenv 15.1.0

- Initial Set-Up
  1. Clone this Repository and Navigate into `needle/needle`
  2. Use the Command `source needle/bin/activate` to launch the Virtual Environment
  3. Use Command `pip install flask` to get the Flask Module.
  4. Use Command `pip install Flask-WTF` to get the WTForms module.
  5. Use Command `pip install mysqlclient` if you're using the MySQL DB
  6. Use `python app.py` to launch the server, and navigate to the local host to interact with the application

  Since this App is in pre-production, the MySQL DB would need an initial setup on your end.

# References

- Flask: http://flask.pocoo.org/docs/0.12/
- WTForms: https://wtforms.readthedocs.io/
- Spotify API: https://developer.spotify.com/web-api/
- Spotipy Client: https://spotipy.readthedocs.io/en/latest/
- MySQL: https://dev.mysql.com/doc/
- Bootstrap: http://getbootstrap.com

Special thanks to the Hack K-State team for hosting a great event!

-Patrick Canny
