from pytyper.core.comparison import (conflicting, matching, chars, conflict_str)

a = "The quick brown fox jumps over the lazy dog."
b = "The quikk bruwn fox jumps ovwr the laxu dog."

def test_conflicting():
	result = conflicting(a, b)
	expected = 5
	assert result == expected

def test_matching():
	result = matching(a, b)
	expected = 39
	assert result == expected

def test_chars():
	result = chars(a, b)
	expected = ["k", "u", "w", "x", "u"]
	assert result == expected

def test_conflict_str():
	result = conflict_str(a, b)
	expected = "       ^    ^               ^        ^^     "
	assert result == expected