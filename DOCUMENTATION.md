# pytyper docs

## Getting started

To install the latest version, run:
```
pip install pytyper
```

## Contents
<!-- (https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#) -->
core
- [calculation](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#calculation)
- [comparison](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#comparison)
- [exceptions](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#exceptions)
- [formatting](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#formatting)

managers
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

The 'calculation' module handles necessary calculations for typing statistics.

##### gross_wpm

`gross_wpm` calculates the user's *gross words-per-minute* by diving the amount of words typed by the amount time it took to type type those characters (disregarding errors). The amount of words typed is not literally the amount of words typed, rather, it is the number of characters typed divided by five. The reasoning for this is because words like 'incomprehensibilities' should count for more than words like 'house' due to the difference in length.

required parameters: **user_input** (*str*), and **seconds** (*float*)

Examples:
```python
user_input = "The quick brown fox jumps over the lazy dog."
seconds = 5.67

gross_wpm(user_input, seconds)
```
Output (*float*):
```
93.12169312169313
```


##### net_wpm
`net_wpm` calculates the user's *net words-per-minute* by subtracting the amount of *errors-per-minute* from the *gross words-per-minute*. This is different from `gross_wpm` as `net_wpm` factors in the amount of errors made.

required parameters (3): **prompt** (*str*), **user_input** (*str*), and **seconds** (*float*)

Examples:
```python
prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors
seconds = 5.67

net_wpm(prompt, user_input, seconds)
```
Output (*float*):
```
40.211640211640216
```

##### accuracy
`accuracy` calculates the user's typing *accuracy* by dividing the number of correctly typed characters by the total number of characters.

required parameters (2): **prompt** (*str*), **user_input** (*str*)

Examples:
```python
prompt = "The quick brown fox jumps over the lazy dog."
user_input = "The quikk bruwn fox jumps ovwr the laxu dog." # 5 errors

accuracy(prompt, user_input)
```
Output (*float*):
```
0.8863636363636364
```
Notes:
It may be helpful to use this function in conjunction with [`to_percentage`](https://github.com/greysonDEV/pytyper/blob/master/DOCUMENTATION.md#to_percentage), which is a method inside of the `formatting` module.

## comparison

## exceptions

## formatting

#### to_percentage

`to_percentage` formats a percentage represented as a float into a percentage represented by a string.

required parameters (1): n (*float*)\
optional parameters (3): **should_round** (*bool*, default: `True`), **up** (*bool*, default: `True`), and **d** (*int*, default `3`)

# Managers

## SessionData

## TestData