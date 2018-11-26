import re


# Hints:
# * The asterisk repeats the previous character 0 or more times
# ”ca*t” matches ”ct”, ”cat”, ”caat”, ”caaat” etc.

# + The plus sign repeats the previous character 1 or more times
# ”ca+t” matches ”cat”, ”caat” etc. but not ”ct”

# ”.” means ”any character” . If you really mean ”.” i.e dot you must use a backslash
# "ca.t" means "cat" , "cabt" , "caat"

# Square brackets mean that any of the listed characters will do
# -> [ab] means either ”a” or ”b”
# -> You can also give a range:
# -> [a-d] means ”a” ”b” ”c” or ”d”
# -> Negation: caret means ”not”
# -> [^a-d] # anything but a, b, c or d

# To match file names like ”hw3.pdf” and ”hw5.txt” ->  hw.\....

# Braces are a more detailed way to indicate repeats
# A{1,3} means at least one and no more than three A’s
# A{4,4} means exactly four A’s

#
# Shortcuts
# Tip1:  \w  which matches “any word character.” --> [a-zA-Z] and it also matches digits, _, and -.
# Tip2:  \d  shortcut matches digit characters. In Python 3, it matches digit characters in other
#            languages. In Python 2, it matches only [0-9].
# Tip3:  \s  shortcut matches whitespace characters, such as space, tab, newline, and so on. The exact
#            list of whitespace characters is greater in Python 3 than in Python 2.
# Tip4:  \b  shortcut matches a zero-length substring. However, it only matches it at the beginning
#            or end of a word. This is called the word boundary character shortcut.

# Question 1
# Write a Python program to check that a string contains only a certain set of
# characters (in this case a-z, A-Z and 0-9).


def check_string(my_string):
	regex = re.compile(r"[A-Za-z0-9.]")
	function_result = regex.search(my_string)
	print("function_result=", function_result)
	return bool(function_result)


print(check_string("A"))
print(check_string("*&%@#!}{"))
print("_________________________________")


# Question 2
# Write a regexp that will match any string that starts with ”hum” and
# ends with ”001” with any number of characters, including none, in between


def check_string(my_string):
	regex = re.compile(r"hum.*001")
	function_result = regex.search(my_string)
	print("function_result=", function_result)
	return bool(function_result)


print(check_string("hum001"))
print(check_string("hum 001"))
print(check_string("hum nahi aaye 001"))
print("_________________________________")


# Question 3
# Write a regexp that will match any Python (.py) file.
# There must be at least one character before the ”.”
# ”.py” is not a legal Python file name

def check_string(my_string):
	regex = re.compile(r".+\.py")
	function_result = regex.search(my_string)
	print("function_result=", function_result)
	return bool(function_result)


print(check_string("file1.txt"))
print(check_string(".py"))
print(check_string("file1.py"))
print("_________________________________")


# Question 4
# Create a regexp which detects legal Microsoft Word file names
# The file name must end with ”.doc” or ”.DOC”
# There must be at least one character before the dot.
# We will assume there are no spaces in the names
# Print out a list of all the legal file names you find
# Test it on testre.txt (on the web site)

def check_string(my_string):
	regex = re.compile(r".+\.[Dd][oO][Cc]")
	function_result = regex.search(my_string)
	print("function_result=", function_result)
	return bool(function_result)


print(check_string("testre.txt"))
print(check_string(".doc"))
print(check_string("file1.Doc"))
print("_________________________________")


# Question : Create a regexp which detects legal Microsoft Word file names which do
# not contain any numerals, and print the location of the first such filename you encounter
# import sys
# import re
# filename = sys.argv[1]
# filehandle = open(filename, "r")
# filecontents = filehandle.read()
# myrule = re.compile(r"[^ 0-9]+\.[dD][oO][cC]")
# match = myrule.search(filecontents)
# print(match.start())

# Question :
# Download & save war_and_peace.txt
# Write py program to read it line-by-line, use
# re.findall to see whether current line contains
# one or more proper names ending in “...ski”;
# print each (but don’t  print [])

file = "war_and_peace.txt"
with open(file, 'r', encoding="utf-8") as myfile:
	for line in myfile:
		x = re.findall(r"[A-Za-z]*ski", line)
		if x:
			print(x)


