from src.player_api import Player

def test_simple_init():
	pl = Player('Raul', 'forward', 7)
	assert pl.last_name == 'Raul'
	assert pl.position == 'forward'
	assert pl.number == 7