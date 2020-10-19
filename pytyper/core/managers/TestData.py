from pytyper.core import calculation
from pytyper.core import comparison

class TestData:
	def __init__(self, prompt, user_input, seconds):
		"""
		Initializer method

		Parameters
		----------
		prompt: str
		user_input: str
		seconds: float
		"""
		self.prompt = prompt
		self.user_input = user_input
		self.seconds = seconds
		self.__fillstats()

	def __fillstats(self):
		"""
		Fills attributes of TestData via necessary calculations
		"""
		self.gross_wpm = calculation.gross_wpm(self.user_input, self.seconds)
		self.net_wpm = calculation.net_wpm(self.prompt, self.user_input, self.seconds)
		self.accuracy = calculation.accuracy(self.prompt, self.user_input)
		self.errors = comparison.conflicting(self.prompt, self.user_input)

		self.numstats = (
			self.gross_wpm,
			self.net_wpm,
			self.accuracy,
			self.errors,
			self.seconds
			)
		self.alphastats = (
			self.prompt,
			self.user_input
			)