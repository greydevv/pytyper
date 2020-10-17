from pytyper.core.managers.TestData import TestData
from pytyper.core.exceptions import allinstance, findillegals

class SessionData:
	def __init__(self, tests):
		if not isinstance(tests, (list, tuple, set)) or not allinstance(tests, TestData):
			raise(TypeError(f'SessionData constructor not properly called!'))
		self._tests = tests
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
			self.averages[keys[curr_key]] = avg
			curr_key += 1

	def get_tests(self):
		return self._tests

	def add_tests(self, tests):
		"""
		Extends _tests with the passed list with members of type TestData.
		"""
		if not isinstance(tests, (list, tuple, set)):
			raise(TypeError(f'add_tests expects either list, tuple, or set'))
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
		Returns a TestData object at the specified index within _tests.
		"""
		try:
			return self._tests[index]
		except IndexError:
			raise(IndexError(f'list index out of range: there is no TestData at position {index}'))
