from pytyper.core.formatting import (round_up, round_down, to_percentage, to_float, match_length, extend_str)

def test_round_up():
	result = round_up(0.25387, 4)
	expected = 0.2539
	assert result == expected

def test_round_down():
	result = round_down(0.25387, 4)
	expected = 0.2538
	assert result == expected

def test_to_percentage():
	result = to_percentage(0.25387, d=4)
	expected = "25.39%"
	assert result == expected

def test_to_float():
	result = to_float("25.39%")
	expected = 0.2539
	assert result == expected

def test_match_length():
	a = "The quick brown fox jumps over the lazy dog."
	b = "The quick brown fox"
	result = match_length(a, b)
	expected = ("The quick brown fox jumps over the lazy dog.", "The quick brown fox                         ")
	assert result == expected

def test_extend_str():
	result = extend_str("The quick brown fox", 25)
	expected = "The quick brown fox                         "
	assert result == expected