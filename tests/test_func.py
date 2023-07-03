import pytest

from main import randint

def test_random():
	assert randint(100) in range(100)


