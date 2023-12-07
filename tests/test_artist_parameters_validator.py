import pytest
from lib.artist_parameters_validator import ArtistParametersValidator

def test_is_valid():
    validator = ArtistParametersValidator("Name", "genre")
    assert validator.is_valid() == True

def test_not_valid():
    validator_1 = ArtistParametersValidator("", "19190")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator(None, "19190")
    assert validator_2.is_valid() == False
    validator_3 = ArtistParametersValidator("Artist", "")


# invalid parameters produces errors

def test_generate_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == ["Artist name must not be blank", "Genre must not be blank"]

def test_get_valid_name_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("", "19190")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Cannot get valid name"

def test_get_valid_genre_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("Taylor", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"

    