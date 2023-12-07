class AlbumParametersValidator:
    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def is_valid(self):
        if not self.is_title_valid():
            return False
        if not self.is_release_year_valid():
            return False
        if not self.is_artist_id_valid():
            return False
        return True
        
    
    def generate_errors(self):
        errors = []
        if not self.is_title_valid():
            errors.append("Title must not be blank")
        if not self.is_release_year_valid():
            errors.append("Release year must not be blank")
        if not self.is_artist_id_valid():
            errors.append("Artist id must not be blank")
        return errors

    def get_valid_title(self):
        if not self.is_title_valid():
            raise ValueError("Cannot get valid title")
        return self.title

    def get_valid_release_year(self):
        if not self.is_release_year_valid():
            raise ValueError("Cannot get valid release year")
        return self.release_year

    def get_valid_artist(self):
        if not self.is_artist_id_valid():
            raise ValueError("Cannot get valid artist id")
        return self.artist_id


    def is_title_valid(self):
        if self.title is None:
            return False
        if self.title == "":
            return False
        return True

    def is_release_year_valid(self):
        if self.release_year is None:
            return False
        if self.release_year == "":
            return False
        return True

    
    def is_artist_id_valid(self):
        if self.artist_id is None:
            return False
        if self.artist_id == "":
            return False
        return True
