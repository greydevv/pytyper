from math import ceil, floor

# Numbers

def round_up(n, d=0):
	"""
	Rounds number n up at d decimal places.
	"""
	mult = 10**d
	return ceil(n*mult)/mult

def round_down(n, d=0):
	"""
	Rounds number n down at d decimal places.
	"""
	mult = 10**d
	return floor(n*mult)/mult

def to_percentage(n, should_round=True, up=True, d=3):
	"""
	Represents a float as a percentage. For example:
	n = 0.25
	s = "25%"
	This method will display
	"""
	if should_round:
		n = round_up(n, d=d) if up else round_down(n, d=d)
	s = f'{n*100}%'
	return s

# Strings

def to_float(s):
	"""
	Converts a percentage represented as a string back into a float. For example:
	s = "33.33%"
	n = 0.3333
	Disclaimer: if n is converted to a string using to_percentage() and then converted back into a float via to_float(), n will have lost precision.
	"""
	n = float(s[:-1])/100
	return n

def match_length(a, b):
	"""
	Matches the lengths of string 'a' and string 'b' by placing blank spaces in the shorter of the two strings
	Used to compare all of the characters. For example, when string 'b' has a lesser length than string 'a':
	a --->  'The quick brown fox jumps over the lazy dog'
	b --->  'The quick brown fox                        '
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

def extend_str(s, n):
	"""
	Concatenates 'n' amount of blank spaces to string 's' via lists
	Used in match_length()
	Not imported by default
	"""
	s = list(s)
	s.extend([' ']*n)
	return ''.join(s)