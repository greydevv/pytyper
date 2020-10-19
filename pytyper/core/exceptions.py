def allinstance(collection, legal_type):
	"""
	Checks the type of all items in a collection match a specified type

	Parameters
	----------
	collection: list, tuple, or set
	legal_type: type

	Returns
	-------
	bool
	"""
	if not isinstance(collection, (list, tuple, set)):
		illegal = type(collection).__name__
		raise(TypeError(f'allinstance expects either list, tuple, or set, not "{illegal}" in first parameter'))
	if not isinstance(legal_type, type):
		raise(TypeError(f'allinstance expects type, not "{legal_type}" in second parameter'))
	return all(isinstance(item, legal_type) for item in collection)

def findillegals(collection, legal_type):
	"""
	Lists the types of items in a collection that do not match the specified type

	Parameters
	----------
	collection: list, tuple, or set
	legal_type: type

	Returns
	-------
	list: str
		returned list is unique i.e., no duplicates
	"""
	if not isinstance(collection, (list, tuple, set)):
		illegal = type(collection).__name__
		raise(TypeError(f'illegaltype expects either list, tuple, or set, not "{illegal}" in first parameter'))
	if not isinstance(legal_type, type):
		illegal = type(legal_type).__name__
		raise(TypeError(f'illegaltype expects type, not instance of "{illegal}" in second parameter'))
	types = [type(item).__name__ for item in collection if type(item) != legal_type]
	return list(set(types))