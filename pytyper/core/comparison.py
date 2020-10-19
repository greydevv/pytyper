from pytyper.core.formatting import match_length

def conflicting(a, b):
	"""
	Totals the number of conflicting characters between two strings

	Parameters
	----------
	a: str
	b: str

	Returns
	-------
	int
	"""
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	d = sum(1 for x,y in comp if x != y)
	return d + diff

def matching(a, b):
	"""
	Totals the number of matching characters between two strings

	Parameters
	----------
	a: str
	b: str

	Returns
	-------
	int
	"""
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	m = sum(1 for x,y in comp if x == y)
	return m - diff

def chars(a, b, match=False):
	"""
	Collects all of the characters that are either matching or conflicting between two strings

	Parameters
	----------
	a: str
	b: str
	match: bool, default False

	Returns
	-------
	list: str
	"""
	a, b = match_length(a, b)
	comp = zip(a, b)
	if match:
		return [y for x,y in comp if x == y]
	else:
		return [y for x,y in comp if x != y]

def conflict_str(a, b, char="^"):
	"""
	Creates a string that is intended to identify errors in a visual manner

	Parameters
	----------
	a: str
	b: str
	char: str, default "^"
	
	Returns
	-------
	str

	Examples
	--------
	a = "The quick brown fox jumps over the lazy dog."
	b = "The quikk bruwn fox jumps ovwr the laxu dog."
	--> "       ^    ^               ^        ^^     "
	"""
	comp = zip(a, b)
	diff = abs(len(a)-len(b))
	conflict_str = []
	for x,y in comp:
		conflict_str.append(" " if x == y else char)
	conflict_str.extend([char]*diff)
	return "".join(conflict_str)