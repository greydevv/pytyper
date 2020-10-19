from math import ceil, floor

# Numbers

def round_up(n, d=0):
	"""
	Rounds a floating point number up to a specified amount of decimal places

	Parameters
	----------
	n: float
	d: int, default 0

	Returns
	-------
	float
	"""
	mult = 10**d
	return ceil(n*mult)/mult

def round_down(n, d=0):
	"""
	Rounds a floating point number down to a specified amount of decimal places

	Parameters
	----------
	n: float
	d: int, default 0

	Returns
	-------
	float
	"""
	mult = 10**d
	return floor(n*mult)/mult

def to_percentage(n, should_round=True, up=True, d=3):
	"""
	Represents a float, rounded up or down to a specified amount of decimal places, as a percentage

	Parameters
	----------
	n: int
	should_round: bool, default True
	up: bool, default True
	d: int, default 3

	Returns
	-------
	str

	Examples
	--------
	n = 0.25
	--> "25.0%"
	"""
	if should_round:
		n = round_up(n, d=d) if up else round_down(n, d=d)
	s = f'{n*100}%'
	return s

# Strings

def to_float(s):
	"""
	Converts a percentage back into a float (essentially the inverse of to_percentage()

	Parameters
	----------
	s: str

	Returns
	-------
	float

	Examples
	--------
	s = "33.33%"
	--> 0.3333
	"""
	n = float(s[:-1])/100
	return n

def match_length(a, b):
	"""
	Matches the lengths of two strings by appending blank spaces to the shorter of the two

	Parameters
	----------
	a: str
	b: str

	Returns
	-------
	tuple: str

	Examples
	--------
	a = "The quick brown fox jumps over the lazy dog."
	b = "The quick brown fox"
	--> "The quick brown fox                         "
	"""
	diff = len(a)-len(b)
	if diff != 0:
		if diff > 0:
			# string 'a' is longer than 'b'
			b = extend_str(b, abs(diff))
		else:
			# string 'b' is longer than 'a'
			a = extend_str(a, abs(diff))
	return a, b

def extend_str(s, n, char=" "):
	"""
	Extends a string by n amount of the specified character

	Parameters
	----------
	s: str

	Returns
	-------
	float

	Examples
	--------
	s = "The quick brown fox"
	n = 25
	--> "The quick brown fox                         "
	"""
	s = list(s)
	s.extend([char]*n)
	return "".join(s)