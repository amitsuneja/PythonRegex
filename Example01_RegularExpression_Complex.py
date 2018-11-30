import re
print(re.search(r'[Pp]ython', 'Python 3'))   # P is CAPITAL

match = re.search(r'([Pp]y)([Tt]h)(o[nf])', 'PyThof 3')
print(match.groups())






"""

Question : You have a phone Book at https://www.python-course.eu/simpsons_phone_book.txt
In above directory some people with the surname Neu.
We are looking for a Neu, but we don't know the first name, we just know that it starts with a J.
Find such people.

"""


import re
import bs4
import requests
import os

my_file = "D:\\abc.txt"
my_url = "https://www.python-course.eu/simpsons_phone_book.txt"
request = requests.get(my_url)
soup = bs4.BeautifulSoup(request.text, "lxml")
data = soup.text

fh = open(my_file, 'w')
fh.write(data)
fh.close()

fh = open(my_file, 'r')
for line in fh:
	if re.search(r"^J.*Neu", line):
		print(line.strip())

fh.close()
os.remove(my_file)

"""
split function

"""
string = "A cat and a rat can't be friends."
print(string.split(" "))


"""
Difference between re.match  and re.findall ?

re.match matches the pattern from the start of the string.  
re.findall however searches for occurrences of the pattern anywhere in the string.

"""
import re
string = "A cat and a rat can't be friends."
print(re.findall(r"\B", string))
print(re.findall(r"\S", string))



"""
Question :below is your string  

'foo=bar,breakfast=spam,eggs,blt=bacon,lettuce,tomato,spam=spam'

You need output, you need to use Regular expression :
[('foo', 'bar'), ('breakfast', 'spam,eggs'), ('blt', 'bacon,lettuce,tomato'), ('spam', 'spam')]

"""
string = 'foo=bar,breakfast=spam,eggs,blt=bacon,lettuce,tomato,spam=spam'

print(re.findall(r'([^=]+)=([^=]+)(?:,|$)', string))
# ([^=]+)    # key -> + means match anything including = sign but by putting [^=]+ we excluded the = sign
# =          # equals is how we tokenise the original string
# ([^=]+)    # value
# (?:,|$)    # value terminator, either comma or end of string





print("___________________________________________________________")


# Look ahead positive (?=)
# A(?=B)  ->Find expression A where expression B follows it

# Look ahead negative (?!)
# A(?!B)  ->Find expression A where expression B does not follow:

# Look behind positive (?<=)
# (?<=B)A ->Find expression A where expression B precedes:

# Look behind negative (?<!)
# (?<!B)A ->Find expression A where expression B does not precede:


#  1. Lookbehind
#  Question : Find all numbers which are not separated from the front word by a white space.

string = "my phone number is010292291, this is a cool phone number: 69530732. Yeah1414757474 is another phone number."
# The naive solution is to use the following regex: [A-Za-z]\d+. This will return all strings that start with a
# letter and many digits after it, and in this case, they are s010292291 and h1414757474.
# And then, we can iterate through them, remove the first character and get the number.
pattern = "([A-Za-z])\d+"  # ['s', 'h']
print(re.findall(pattern, string))
pattern = "(?:[A-Za-z])\d+"  # ['s010292291', 'h1414757474']
print(re.findall(pattern, string))


# But that does not seem to be a very good solution. Why we have to manually remove the first letter?
# Why we can not just get the number I need without the letter? That's when we need to use Lookbehind.
# The expression (?<=[A-Za-z]) is called lookbehind expression
# (?<=B)A ->Find expression A where expression B precedes:
pattern = "(?<=[A-Za-z])\d+"
print(re.findall(pattern, string))  # ['010292291', '1414757474']

print("______________________________________________________")

# 2. Lookahead
# It is basically the same as lookbehind, the only difference is it matches characters at the
# end of the string. The syntax is slightly different, we use (?!)
# A(?!B)  ->Find expression A where expression B does not follow:
pattern = "\d+(?![A-Za-z])"
print(re.findall(pattern, string))  # ['010292291', '69530732', '1414757474']
print("______________________________________________________")

string = "Andy Smith, Jim Brown, Lisa Smith, Sue Brown, Amit    , Raj."
# Look ahead positive (?=)
# A(?=B) A where expression B follows:
pattern = r"\w+(?=\sBrown,)"
print(re.findall(pattern, string))

print("______________________________________________________")

# A(?=B)
pattern = "\w+\s*\w*(?=[,.])"
print(re.findall(pattern, string))



