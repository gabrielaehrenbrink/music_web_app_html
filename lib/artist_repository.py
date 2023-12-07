from lib.artist import Artist


class ArtistRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection


    def all_artists(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists
    
    def create_artist(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        artist.id = rows[0]['id']
        return None

    def find_artist(self, artist_id):
        rows = self._connection.execute("SELECT * FROM artists WHERE id = %s", [artist_id])
        row = rows[0]
        return Artist(row['id'], row['name'], row['genre'])
