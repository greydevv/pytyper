from pytyper.core.exceptions import (allinstance, findillegals)

def test_allinstance():
	collection = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
	result = allinstance(collection, str)
	expected = True
	assert result == expected

def test_findillegals():
	collection = ["The", "quick", 1, ["b", "r", "o", "w", "n"], "fox", "jumps", "over", "the", "lazy", "dog."]
	result = findillegals(collection, str)
	expected = ["int", "list"]
	assert result == expected