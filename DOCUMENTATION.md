# pytyper docs

## Getting started

To install the latest version, run:
```
pip install pytyper
```

## Contents
- [core](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#core)
  - [calculation](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#calculation)
    - [gross_wpm](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#gross_wpm)
    - [net_wpm](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#net_wpm)
    - [accuracy](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#accuracy)
  - [comparison](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#comparison)
    - [conflicting](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#conflicting)
    - [matching](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#matching)
    - [chars](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#chars)
    - [conflict_str](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#conflict_str)
  - [exceptions](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#exceptions)
    - [allinstance](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#allinstance)
    - [findillegals](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#formattinng)
  - [formatting](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#formatting)
    - [round_up](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#round_up)
    - [round_down](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#round_down)
    - [to_percentage](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#to_percentage)
    - [to_float](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#to_float)
    - [match_length](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#match_length)
    - [extend_str](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#extend_str)
- [managers](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#managers)
  - [SessionData](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#SessionData)
  - [TestData](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#TestData)

## Other
A proof-of-concept CLI tool is hosted at:\
https://github.com/greysonDEV/typeshell-cli

------
<br>
<br>

# Core

## calculation

### gross_wpm

`gross_wpm` calculates the user's *gross words-per-minute* by diving the amount of words typed by the amount time it took to type type those characters (disregarding errors). The amount of words typed is not literally the amount of words typed, rather, it is the number of characters typed divided by five. The reasoning for this is because words like 'incomprehensibilities' should count for more than words like 'house' due to the difference in length.

- Required parameters (2):
  - **user_input** (*str*)
  - **seconds** (*float*)

Examples:
```python
user_input = "The quick brown fox jumps over the lazy dog."
seconds = 5.67

gross_wpm(user_input, seconds)
```
Output (*float*):
```python
93.12169312169313
```

### net_wpm

`net_wpm` calculates the user's *net words-per-minute* by subtracting the amount of *errors-per-minute* from the *gross words-per-minute*. This is different from `gross_wpm` as `net_wpm` factors in the amount of errors made.

- Required parameters (3):
  - **prompt** (*str*)
  - **user_input** (*str*)
  - **seconds** (*float*)

Examples:
```python
prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors
seconds = 5.67

net_wpm(prompt, user_input, seconds)
```
Output (*float*):
```python
40.211640211640216
```

### accuracy

`accuracy` calculates the user's typing *accuracy* by dividing the number of correctly typed characters by the total number of characters.

- Required parameters (2):
  - **prompt** (*str*)
  - **user_input** (*str*)

Examples:
```python
prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors

accuracy(prompt, user_input)
```
Output (*float*):
```python
0.8863636363636364
```
Notes:\
It may be helpful to use this function in conjunction with [`to_percentage`](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#to_percentage), which is a method inside of the `formatting` module.
<br>

## comparison

### conflicting

`conflicting` totals the number of characters in string **b** that do not match their pair in string **a**.

- Required parameters (2):
  - **a** (*str*)
  - **b** (*str*)

Examples:
```python
a = "The quick brown fox jumps over the lazy dog."
b = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 differences

conflicting(a, b)
```
Output (*int*):
```python
5
```
Notes:\
`conflicting` will also account for missing characters, i.e. if string **b** has a different length than string **a**, that difference is added to the total number of characers that do not match their pairs.

### matching

`matching` totals the number of characters in string **b** that match their pair in string **a**.

- Required parameters (2):
  - **a** (*str*)
  - **b** (*str*)

Examples:
```python
a = "The quick brown fox jumps over the lazy dog."
b = "The quikk bruwn fox jumps ovwr the laxu dog." # 39 matches

conflicting(a, b)
```
Output (*int*):
```python
39
```

### chars

`chars` creates a list of all of the characters in string **b** that are either conflicting or matching with their pair in string **a**.

- Required parameters (2):
  - **a** (*str*)
  - **b** (*str*)

Examples:
```python
a = "The quick brown fox jumps over the lazy dog."
b = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors

chars(a, b, match=False)
chars(a, b, match=True)
```
Output (*int*):
```python
["k", "u", "w", "x", "u"] # conflicting
["T", "h", "e", "q", "u", "i", "k", " ", "b", "r", "w", "n", " ", "f", "o", "x", "j", "u", "m", "p", "s", " ", "o", "v", "r", " ", "t", "h", "e", " ", "l", "a", " ", "d", "o", "g"]
```

### conflict_str

`conflict_str` creates a string with a specified character at the each index position in which a character in string **b** does not match its pair in string **a**.

- Required parameters (2):
  - **a** (*str*)
  - **b** (*str*)
- Optional parameters (1):
  - **char** (*str*, default: `"^"`)

Examples:
```python
a = "The quick brown fox jumps over the lazy dog."
b = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors

conflict_str(a, b)
```
Output (*int*):
```python
# "The quick brown fox jumps over the lazy dog."
# "The quikk bruwn fox jumps ovwr the laxu dog."
  "       ^    ^               ^        ^^     "
```
<br>

## exceptions

### allinstance

`allinstance` checks whether or not each item in a collection is of a specified type.

- Required parameters (2):
  - **collection** (*list*, *tuple*, *set*)
  - **legal_type** (*type*)

Examples:
```python
collection = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

allinstance(collection, str)
```
Output (*bool*):
```python
True
```

### findillegals

`findillegals` gathers a unique list of the types (represented as strings) in a collection that do not match a specified type.

- Required parameters (2):
  - **collection** (*list*, *tuple*, *set*)
  - **legal_type** (*type*)

Examples:
```python
collection = ["The", "quick", 1, ["b", "r", "o", "w", "n"], "fox", "jumps", "over", "the", "lazy", "dog."]

findillegals(collection, str)
```
Output (*list*: *str*):
```python
["int", "list"]
```
<br>

## formatting

### round_up

`round_up` will round a float up to a specified amount of decimal places.

- Required parameters (1):
  - **n** (*float*)
- Optional parameters (1):
  - **d** (*int*, default: `0`)

Examples:
```python
n = 0.8732

round_up(n, d=2)
```
Output (*float*):
```python
0.88
```

### round_down

`round_down` will round a float down to a specified amount of decimal places.

- Required parameters (1):
  - **n** (*float*)
- Optional parameters (1):
  - **d** (*int*, default: `0`)

Examples:
```python
n = 0.8732

round_down(n, d=2)
```
Output (*float*):
```python
0.87
```

### to_percentage

`to_percentage` formats a percentage represented as a float into a percentage represented by a string.

- Required parameters (1):
  - **n** (*float*)
- Optional parameters (3):
  - **should_round** (*bool*, default: `True`)
  - **up** (*bool*, default: `True`)
  - **d** (*int*, default `3`)

Examples:
```python
n = 0.8863636363636364

to_percentage(n)
```
Output (*str*):
```python
"88.7%"
```

### to_float

`to_float` converts a percentage back into a float. This operation is essentially the inverse of `to_percentage`.

- Required parameters (1):
  - **s** (*str*)

Examples:
```python
s = "88.7%"

to_float(s)
```
Output (*float*):
```python
0.887
```

### match_length

`match_length` matches the lengths of two strings by concatenating a number of blank spaces to the shorter string. The number of blanks spaces is determined by the difference in characters in the two strings.

- Required parameters (2):
  - **a** (*str*)
  - **b** (*str*)

Examples:
```python
a = "The quick brown fox jumps over the lazy dog."
b = "The quick brow fox"

match_length(a, b)
```
Output (*tuple*):
```python
# "The quick brown fox jumps over the lazy dog."
# "The quick brown fox                         "
("The quick brown fox jumps over the lazy dog.", "The quick brown fox                         ")
```

### extend_str

`extend_str` concatenates a specified amount of spaces to the end of a string. This is used primarily by `match_length`.

- Required parameters (2):
  - **s** (*str*)
  - **n** (*n*)
- Optional parameters (1):
  - **char** (*str*, default: `" "`)

Examples:
```python
a = "The quick brown fox"

extend_str(a, 25, char="-")
```
Output (*str*):
```python
"The quick brown fox-------------------------"
```
<br>

# Managers

## SessionData

`SessionData` is a pytyper class that is effective in managing all typing tests and statistics for a typing session. It is also responsible for calculating the average of all of the numerical statistics for the entire session.

### initializer

- Required parameters (1):
  - **tests** (*list*: *TestData*)
- Optional parameters (1):
  - **round_stats** (*bool*, default: `True`)

Examples:
```python
tests = [
	TestData("Actions speak louder than words.", "Actions speak louder than words.", 4.58),
	TestData("A fool and his money are soon parted.", "A fool anf his miney are soon partid.", 3.53),
	TestData("Appearances can be deceptive.", "Appesrances csn be deciptive.", 2.62)
	]

sd = SessionData(tests)
```

Exceptions:\
The required parameter, **tests**, must be a list of type TestData. This is required for the success of calculations done on the statistics across all tests taken within this session. Therefore, the initializer will raise an exception if the types all of the items in the list are not of type TestData:

> TypeError: SessionData constructor not properly called!

### add_tests

`add_tests` adds a list of tests to SessionData's existing list of tests.

- Required parameters (1):
  - **tests** (*list*: *TestData*)

Examples
```python
new_tests = [
	TestData("Absence makes the heart grow fonder.", "Absence makes the heart grow fonder.", 5.62),
	TestData("A stitch in time saves nine.", "A stitch in time saves nine.", 4.68)
	]

sd.add_tests(new_tests)
```

Exceptions:\
If the required parameter, **tests**, is not of type list, an exception is raised:

> TypeError: add_tests expects list

In addition, if the list is empty, an exception is raised:

> ValueError: 0 tests passed, expects a minimum of 1

Finally, if the entirety of the items in the list are not of type TestData, an exception is raised:

> TypeError: can only pass collection of TestData, not "{illegal}"

### get_test

`get_test` returns an object of type TestData from SessionData's existing list of tests at a specified index.

- Required parameters (1):
  - **index** (*int*)

Examples:
```python
tests = [
	TestData("Actions speak louder than words.", "Actions speak louder than words.", 4.58),
	TestData("A fool and his money are soon parted.", "A fool anf his miney are soon partid.", 3.53),
	TestData("Appearances can be deceptive.", "Appesrances csn be deciptive.", 2.62)
	]

sd = SessionData(tests)

sd.get_test(2)
```
Output (*TestData*):
```python
<pytyper.core.managers.TestData.TestData object at MEMORY_ADDRESS>
```

Exceptions:\
If the required parameter, **index**, is outside of the SessionData's list of tests, an exception is raised:

> IndexError: list index out of range: there is not TestData at position {index}

<br>

## TestData

`TestData` is a pytyper class that is effective in managing statistics for a particular typing test.

### initialzier

- Required parameters (3):
  - **prompt** (*str*)
  - **user_input** (*str*)
  - **seconds** (*str*)
- Accessible attributes (7):
  - **prompt** (*str*)
  - **user_input** (*str*)
  - **seconds** (*float*)
  - **gross_wpm** (*float*)
  - **net_wpm** (*float*)
  - **accuracy** (*float*)
  - **errors** (*int*)




