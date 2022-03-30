import pytest

from activity.main import *

def test_exception_not_raised():
    result = having_an_exception("Some country name")
    assert result is True

def test_exception():
    with pytest.raises(ValueError):
        having_an_exception("Texas")


# Ex.2
# def test_empty_dict_raises_keyerror():
#     movies = {}

#     with pytest.raises(KeyError):
#         valid_movie = find_shrek_2(movies)