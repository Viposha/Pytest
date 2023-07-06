import pytest
import random

@pytest.fixture()
def list_creator():
	return [n for n in range(1,11)]

@pytest.fixture(scope='module')
def number_fixture():
	"""Generate number in range 100"""
	print('start')
	yield random.choice(range(100))
	print('finish')


def test_list(list_creator):
	assert len(list_creator) == 10

def test_number(number_fixture):
	assert number_fixture in range(100)

def test_positiv_number(number_fixture):
	assert number_fixture > 0