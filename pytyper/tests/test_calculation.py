from pytyper.core.calculation import (gross_wpm, net_wpm, accuracy)

prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog."
seconds = 5.5

def test_gross_wpm():
	result = gross_wpm(user_input, seconds)
	expected = (44/5)/(seconds/60)
	assert result == expected

def test_net_wpm():
	result = net_wpm(prompt, user_input, seconds)
	expected = (44/5)/(seconds/60) - (5/(seconds/60))
	assert result == expected

def test_accuracy():
	result = accuracy(prompt, user_input)
	expected = (39/44)
	assert result == expected



prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog."
seconds = 5.67
print(accuracy(prompt, user_input))