from src.player_api import Player

def test_simple_init():
	pl = Player('Raul', 'forward', 7)
	assert pl.last_name == 'Raul'
	assert pl.position == 'forward'
	assert pl.number == 7

def test_default_init():
	pl = Player()
	assert pl.last_name is None
	assert pl.position is None
	assert pl.number is None

def test_equality():
	pl1 = Player('Raul', 'forward', 7)
	pl2 = Player('Raul', 'forward', 7)
	assert pl1 == pl2

def test_equality_diff_name():
	pl1 = Player('Raul', 'forward', 15)
	pl2 = Player('Raul', 'forward', 7)
	assert pl1 == pl2


def test_to_dict():
	pl1 = Player('Raul', 'forward', 15)
	pl2 = pl1.to_dict()
	pl2_expected = {
		'last_name': 'Raul',
		'position': 'forward',
		'number': 15,
	}
	assert pl2 == pl2_expected


def test_isinstance():
	pl1 = Player('Raul', 'forward', 15)
	assert isinstance(pl1, Player) == True