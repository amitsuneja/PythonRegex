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