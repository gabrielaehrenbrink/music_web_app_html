from playwright.sync_api import Page, expect


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        'Doolittle\n',
        'Surfer Rosa\n', 
        'Waterloo\n',
        'Super Trouper\n',
        'Bossanova\n', 
        'Lover\n',
        'Folklore\n',
        'I Put a Spell on You\n',
        'Baltimore\n', 
        'Here Comes the Sun\n', 
        'Fodder on My Wings\n', 
        'Ring Ring\n'
    ])


# Test-drive and implement a route that returns the HTML content for a single album
def test_get__album(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums/show/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('Album: Doolittle\n')



# Test a route GET /artists/<id> which returns an HTML page showing details for a single artist. 

def test_get_artist_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/artists.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    h1_tag = page.locator("h1")
    h1_tag.wait_for()
    print(h1_tag)
    expect(h1_tag).to_have_text("Artist: Taylor Swift \n")


# Test a route GET /artists which returns an HTML page with the list of artists. 
# This page should contain a link for each artist listed, linking to /artists/<id> where 
# <id> needs to be the corresponding artist id 
def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/artists.sql")
    page.goto(f"http://{test_web_address}/artists")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        'Pixies\n', 
        '\nABBA\n', 
        '\nTaylor Swift\n', 
        '\nNina Simone\n'])


# Test-drive and implement a form page to add a new album.
# You should then be able to use the form in your web browser to add a new album, 
# and see this new album in the albums list page.
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add Album"')
    page.fill("input[name='title']", "Reputation")
    page.fill("input[name='release_year']", "2017")
    page.fill('input[name="artist_id"]', "3")
    page.click("text=Create Album")

    h1_tag = page.locator('h1')
    print(h1_tag)
    expect(h1_tag).to_have_text("Album: Reputation")

    release_year_tag = page.locator('p')
    expect(release_year_tag).to_have_text('Released year: 2017')

def test_validate_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")    
    page.click('text="Add Album"')
    page.click('text="Create Album"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title must not be blank, " \
        "Release year must not be blank, " \
        "Artist id must not be blank"
    )


# Test-drive and implement a form page to add a new artist.
# You should then be able to use the form in your web browser to add a new artist, 
# and see this new artist in the albums list page.
def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/artists.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Add Artist"')
    page.fill("input[name='name']", "The Beatles")
    page.fill("input[name='genre']", "Rock")
    page.click("text=Create Artist")

    h1_tag = page.locator('h1')
    print(h1_tag)
    expect(h1_tag).to_have_text("Artist: The Beatles")

    release_year_tag = page.locator('p')
    expect(release_year_tag).to_have_text('Genre: Rock')




# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
