from pytyper.core.managers.TestData import TestData

prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog."
seconds = 5.5

def test_TestData():
	td = TestData(prompt, user_input, seconds)
	result = (td.numstats, td.alphastats)
	expected = (
		((44/5)/(seconds/60), (44/5)/(seconds/60) - (5/(seconds/60)), (39/44), 5, 5.5),
		(prompt, user_input)
		)
	assert result == expected
