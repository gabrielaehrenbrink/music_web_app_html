import pytest
from lib.album_parameters_validator import AlbumParametersValidator

def test_is_valid():
    validator = AlbumParametersValidator("My title", "19190", 5)
    assert validator.is_valid() == True

def test_not_valid():
    validator_1 = AlbumParametersValidator("", "19190", 1)
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator(None, "19190", 1)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("My title", "", 4)
    assert validator_3.is_valid() == False
    validator_4 = AlbumParametersValidator("My title", None, 3)
    assert validator_4.is_valid() == False

# invalid parameters produces errors

def test_generate_errors():
    validator_1 = AlbumParametersValidator("", "", 5)
    assert validator_1.generate_errors() == ["Title must not be blank", "Release year must not be blank"]

def test_get_valid_title_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("", "19190", 3)
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_title()
    assert str(err.value) == "Cannot get valid title"

def test_get_valid_release_year_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("Reputation", "", 6)
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"

    


