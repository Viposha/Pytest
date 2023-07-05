""" Create api for player"""

from dataclasses import dataclass, asdict, field


@dataclass
class Player:
	last_name: str = None
	position: str = None
	number: int = field(default=None, compare=False)

	@classmethod
	def from_dict(cls, d):
		return Player(**d)
	def to_dict(self):
		return asdict(self)




