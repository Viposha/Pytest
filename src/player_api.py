""" Create api for player"""

from dataclasses import dataclass, asdict


@dataclass
class Player:
	last_name: str = None
	position: str = None
	number: int = None

	@classmethod
	def to_dict(self):
		return asdict(self)
