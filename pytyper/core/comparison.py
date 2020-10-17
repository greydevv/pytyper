from pytyper.core.formatting import match_length

def conflicting(a, b):
	'''
	Compares two strings against each other and returns the number of characters that do not match.
	'''
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	d = sum(1 for x,y in comp if x != y)
	return d + diff

def matching(a, b):
	'''
	Compares two strings against each other and returns the number of characters that match.
	'''
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	m = sum(1 for x,y in comp if x == y)
	return m - diff

def chars(a, b, match=False):
	'''
	Returns the characters in string 'b' that do not match their pair in string 'a'
	'''
	a, b = match_length(a, b)
	comp = zip(a, b)
	if match:
		return [y for x,y in comp if x == y]
	else:
		return [y for x,y in comp if x != y]

def conflict_str(a, b, char='^'):
	'''
	Creates a string that indicates differenes in two strings by placing a specified char at the location of errors.
	This string is intended to be placed underneath of the user input. For example:
	a            ---> 'The quick brown fox jumps over the lazy dog.'
	b            ---> 'The qyick brown fox jumls ober the lazu dpg.'
	conflict_str ---> '     ^                 ^   ^          ^  ^  '
	'''
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	conflict_str = []
	for x,y in comp:
		conflict_str.append(' ' if x == y else char)
	conflict_str.extend([char]*diff)
	return ''.join(conflict_str)









