from pytyper.core.comparison import conflicting, matching

def gross_wpm(user_input, seconds):
	"""
	Calculates the user's gross WPM (words per minute).
	Gross WPM is found by dividing the number of characters typed divided by 5 over a given amount of time.
	Gross WPM will not give the most accurate WPM as the number of errors are not factored in.
	The number of characters typed is divided by 5 as typing longer words should count more than short words.
	"""
	gross = (len(user_input)/5)/(seconds/60)
	return gross

def net_wpm(prompt, user_input, seconds):
	"""
	Calculates the user's net WPM (words per minute) for a given prompt.
	Net WPM is found by subtracting the number of uncorrected errors over a given amount of time from the Gross WPM.
	Net WPM will give the most accurate WPM as the number of errors are factored in.
	Net WPM cannot be negative, so 0 will be returned instead.
	"""
	net = gross_wpm(user_input, seconds) - (conflicting(prompt, user_input)/(seconds/60))
	return net if net > 0 else 0

def accuracy(prompt, user_input):
	"""
	Calculates the user's typing accuracy for a given prompt.
	Accuracy is found by dividing the number of correctly typed characters by the total amount of characters typed.
	Accuracy cannot be negative, so 0 will be returned instead.
	"""
	if len(user_input) < 1:
		return 0
	a = matching(prompt, user_input)/len(user_input)
	return a if a > 0 else 0