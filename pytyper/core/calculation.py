from pytyper.core.comparison import conflicting, matching

def gross_wpm(user_input, seconds):
	"""
	Calculates gross words-per-minte

	Parameters
	----------
	user_input: str
	seconds: float or int

	Returns
	-------
	float
	"""
	gross = (len(user_input)/5)/(seconds/60)
	return gross

def net_wpm(prompt, user_input, seconds):
	"""
	Calculates net words-per-minute

	Parameters
	----------
	prompt: str
	user_input: str
	seconds: float or int

	Returns
	-------
	float
	"""
	net = gross_wpm(user_input, seconds) - (conflicting(prompt, user_input)/(seconds/60))
	return net if net > 0 else 0

def accuracy(prompt, user_input):
	"""
	Calculates the percentage difference of two strings for accuracy

	Parameters
	----------
	prompt: str
	user_input: str

	Returns
	-------
	float
	"""
	if len(user_input) < 1:
		return 0
	a = matching(prompt, user_input)/len(user_input)
	return a if a > 0 else 0


