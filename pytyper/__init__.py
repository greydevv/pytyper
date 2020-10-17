"""
pytype

This package aims to aid in the creation and analysis of typing test by fitting the user with the necessary calculations for WPM, accuracy, etc.

Author: Greyson Murray
"""

from pytyper.core.calculation import (
	gross_wpm,
	net_wpm,
	accuracy,
)

from pytyper.core.comparison import (
	conflicting,
	matching,
	chars,
	conflict_str,
)

from pytyper.core.formatting import (
	round_up,
	round_down,
	to_percentage,
	to_float,
	match_length
)

from pytyper.core.managers.TestData import TestData
from pytyper.core.managers.SessionData import SessionData
