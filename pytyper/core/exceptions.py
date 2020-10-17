def allinstance(collection, legal_type):
	"""
	Checks if all items in 'collection' (list, tuple, set) matches the 'legal_type' argument.
	"""
	if not isinstance(collection, (list, tuple, set)):
		illegal = type(collection).__name__
		raise(TypeError(f'allinstance expects either list, tuple, or set, not "{illegal}" in first parameter'))
	if not isinstance(legal_type, type):
		raise(TypeError(f'allinstance expects type, not "{legal_type}" in second parameter'))
	return all(isinstance(item, legal_type) for item in collection)

def findillegals(collection, legal_type):
	"""
	Returns a list of all of the unique types in 'collection' (list, tuple, set) that do not match the 'legal_type' argument.
	"""
	if not isinstance(collection, (list, tuple, set)):
		illegal = type(collection).__name__
		raise(TypeError(f'illegaltype expects either list, tuple, or set, not "{illegal}" in first parameter'))
	if not isinstance(legal_type, type):
		illegal = type(legal_type).__name__
		raise(TypeError(f'illegaltype expects type, not instance of "{illegal}" in second parameter'))
	types = [type(item).__name__ for item in collection if type(item) != legal_type]
	return list(set(types))