import random

def randint(n):

	""" Return random int number in range (n)"""

	return random.choice(range(n))

if __name__ == "__main__":
	randint(random.choice(range(100)))