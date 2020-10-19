from pytyper.core.managers.SessionData import SessionData
from pytyper.core.managers.TestData import TestData

tests = [
	TestData("Actions speak louder than words.", "Actions speak louder than words.", 4.58),
	TestData("A fool and his money are soon parted.", "A fool anf his miney are soon partid.", 3.53),
	TestData("Appearances can be deceptive.", "Appesrances csn be deciptive.", 2.62)
	]
sd = SessionData(tests)

def test_SessionData_averages():
	result = sd.averages
	expected = {
		"gross_wpm": 114.149,
		"net_wpm": 74.251,
		"accuracy": 0.939,
		"errors": 2.0,
		"seconds": 3.577
		}
	assert result == expected

def test_SessionData_get_tests():
	result = sd.get_tests()
	expected = tests
	assert result == expected

def test_SessionData_add_tests():
	new_tests = [
		TestData("Absence makes the heart grow fonder.", "Absence makes the heart grow fonder.", 5.62),
		TestData("A stitch in time saves nine.", "A stitch in time saves nine.", 4.68)
		]
	result = sd.add_tests(new_tests)
	expected = tests.extend(new_tests)
	assert result == expected

def test_SessionData_get_test():
	result = sd.get_test(2)
	expected = tests[2]
	assert result == expected