import pytest

from image_service import ImageDownloader
from requests import RequestException

@pytest.fixture
def checker():
    return ImageDownloader()


def test_is_image(checker):
    assert checker.is_image(checker.get_bytes(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Coat_types_3.jpg/1280px-Coat_types_3.jpg")) is True
    assert checker.is_image(checker.get_bytes(
        "https://pngimg.com/uploads/dog/dog_PNG50260.png")) is True
    assert checker.is_image(checker.get_bytes(
        "https://media.giphy.com/media/Pn1gZzAY38kbm/giphy.gif")) is True


def test_is_not_image(checker):
    assert checker.is_image(checker.get_bytes("https://en.wikipedia.org/wiki/PDF")) is False
    assert checker.is_image(checker.get_bytes("https://en.wikipedia.org/wik")) is False


def test_with_exception(checker):
    with pytest.raises(RequestException):
        checker.is_image(checker.get_bytes("ftp://en.wikipedia.org/wik"))
