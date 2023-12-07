class ArtistParametersValidator:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def is_valid(self):
        if not self.is_name_valid():
            return False
        if not self.is_genre_valid():
            return False
        return True
        
    
    def generate_errors(self):
        errors = []
        if not self.is_name_valid():
            errors.append("Artist name must not be blank")
        if not self.is_genre_valid():
            errors.append("Genre must not be blank")
        return errors

    def get_valid_name(self):
        if not self.is_name_valid():
            raise ValueError("Cannot get valid name")
        return self.name

    def get_valid_genre(self):
        if not self.is_genre_valid():
            raise ValueError("Cannot get valid genre")
        return self.genre


    def is_name_valid(self):
        if self.name is None:
            return False
        if self.name == "":
            return False
        return True

    def is_genre_valid(self):
        if self.genre is None:
            return False
        if self.genre == "":
            return False
        return True

