import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist
from lib.album_parameters_validator import AlbumParametersValidator
from lib.artist_parameters_validator import ArtistParametersValidator


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all() 
    return render_template("albums/index.html", albums=albums)  


@app.route('/albums/show/<id>', methods=['GET'])
def get_album(id): 
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/show.html", album=album)


# Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.    

@app.route('/artists/<id>', methods=['GET'])
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find_artist(id)
    return render_template("artists/artist.html", artist=artist)


# Add a route GET /artists which returns an HTML page with the list of artists. 
# This page should contain a link for each artist listed, linking to /artists/<id> where 
# <id> needs to be the corresponding artist id    

@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all_artists()
    return render_template('artists/allartists.html', artists=artists)

# GET /albums/new
# Returns a form to create a new album
@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')

# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    validator = AlbumParametersValidator(
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id']
    )

    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)

    album = Album(
        None, 
        validator.get_valid_title(), 
        validator.get_valid_release_year(),
        validator.get_valid_artist())

# Save the album to the database
    repository.create(album)

# Redirect to the albums's show route to the user can see it
    return redirect(f"/albums/show/{album.id}")


# GET /albums/new
# Returns a form to create a new album
@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new_artist.html')


@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    validator = ArtistParametersValidator(
        request.form['name'],
        request.form['genre']
    )

    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("artists/new.html", errors=errors)

    artist = Artist(
        None, 
        validator.get_valid_name(), 
        validator.get_valid_genre())

# Save the album to the database
    repository.create_artist(artist)

# Redirect to the albums's show route to the user can see it
    return redirect(f"/artists/{artist.id}")














# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
