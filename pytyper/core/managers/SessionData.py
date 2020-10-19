from pytyper.core.managers.TestData import TestData
from pytyper.core.exceptions import allinstance, findillegals
from pytyper.core.formatting import round_up

class SessionData:
	def __init__(self, tests, round_stats=True):
		"""
		Initializer method

		Parameters
		----------
		tests: list: TestData
		round_stats: bool, default True
		"""
		if not isinstance(tests, list) or not allinstance(tests, TestData):
			raise(TypeError(f'SessionData constructor not properly called!'))
		self._tests = tests
		self.round_stats = round_stats
		self.averages = {}
		if len(tests) > 0:
			self.__setaverages()

	def __setaverages(self):
		"""
		Averages each numerical statistic of each TestData.
		"""
		stats = [test.numstats for test in self._tests]
		keys = ['gross_wpm', 'net_wpm', 'accuracy', 'errors', 'seconds']
		curr_key = 0
		for stat in zip(*stats):
			avg = (sum([i for i in stat])/len(stat))
			self.averages[keys[curr_key]] = round_up(avg, 3) if self.round_stats else avg
			curr_key += 1

	def get_tests(self):
		"""
		Getter for _tests

		Returns
		-------
		list: TestData
		"""
		return self._tests

	def add_tests(self, tests):
		"""
		Adds tests to _tests via list extension

		Parameters
		----------
		tests: list: TestData
		"""
		if not isinstance(tests, list):
			raise(TypeError(f'add_tests expects list'))
		elif len(tests) == 0:
			raise(ValueError(f'0 tests passed, expects a minimum of 1'))
		elif not allinstance(tests, TestData):
			illegal = findillegals(tests, TestData)[0]
			raise(TypeError(f'can only pass collection of TestData, not "{illegal}"'))
		else:
			self._tests.extend(tests)
			self.__setaverages()

	def get_test(self, index):
		"""
		Getter for specific test in _tests at specified index

		Parameters
		----------
		index: int

		Returns
		-------
		TestData
		"""
		try:
			return self._tests[index]
		except IndexError:
			raise(IndexError(f'list index out of range: there is no TestData at position {index}'))
