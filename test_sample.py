from unittest.mock import MagicMock, patch

from sample import Dog


class TestSample:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2

    def test_dog_bark(self):
        d = Dog()
        assert d.bark() == "barkkkk"


    def test_dog_bark_with_magic_mock(self):
        d = Dog()
        d.bark = MagicMock(return_value="meow")
        assert d.bark() == "meow"

