"""
Regular expression:

"""
import re

"""
Tip1 : 
1. Never use re.match, instead use re.search with ^ (^ at beginning is like start of line and $ means end of line )
Its is good to remember that re.match will always match from begining of string

2. re.search will return the first match object and ignore the rest match.
3. Alternate is re.findall , re.findall will return list
4. Other Alternate is re.finditer return the interator
5. You can denote a character class by using square brackets [pP],[ae] and listing the possible characters 
within the brackets.
6. r"[pP]ython" , r"gr[ae]y" . Here r is for raw. The difference between a raw string and a regular string is 
simply that raw strings do not interpret the \ character as an escape character.

"""


print(re.search(r'[Pp]ython', 'Python 3'))   # P is CAPITAL
print(re.search(r'[Pp]ython', 'python 3'))   # p is small
print(re.search(r'[Pp]ython', 'PYTHON 3'))   # None for PYTHON

print(re.search(r"gr[ae]y",  'gray'))        # matched gray
print(re.search(r"gr[ae]y",  'grey'))        # grey
print(re.search(r"gr[ae]y",  'gray and grey'))   # but return the first match.
print(re.findall(r"gr[ae]y",  'gray and grey'))  # alternate is re.findall , return list
print(re.finditer("gr[ae]y", 'gray and grey'))   # or re.finditer , return interator.

print(re.search(r"[a-zA-Z0-9]", '99'))    # r"[a-zA-Z0-9]" this is range a to z OR A to Z OR 0 to 9 any digit
print(re.search(r"[a-zA-Z0-9\-]", '-'))   # notice i need to search alphanumeric characters, hyphen and i used \-
print(re.search(r"[a-zA-Z0-9\@]", '@'))   # notice i need to search alphanumeric characters, @ and i used \@
print(re.search(r"[a-zA-Z0-9\_]", '_'))   # notice i need to search alphanumeric characters, underscore and i used \-
print(re.search(r"[a-zA-Z0-9\\]", "\\"))  # A very special case
print(re.search(r"[a-zA-Z0-9']", "'"))    # to search ' i did not use \' as escaping is not required at it make read tuff




"""
Negation:
You can invert a character class (meaning that it will match any character other than those specified)
by beginning the character class with a ^ character.

"""
# Consider the regular expression n[^e]. This means the character n followed by any character that is not an e.
print(re.search(r'n[^e]', 'final'))  # return "na" match object
print(re.search(r'n[^e]', 'jasmine')) # return None , Here, the regular expression engine gets to the only n in the
                                      # string but cannot match the next character, because it is an e . Hence no match

# However, the regular expression also will not match against an n at the end of the string.
print(re.search(r'n[^e]', 'Python'))  # None







"""
Shortcuts
Tip1:  \w  which matches “any word character.” --> [a-zA-Z] and it also matches digits, _, and -.
Tip2:  \d  shortcut matches digit characters. In Python 3, it matches digit characters in other
           languages. In Python 2, it matches only [0-9].
Tip3:  \s  shortcut matches whitespace characters, such as space, tab, newline, and so on. The exact
           list of whitespace characters is greater in Python 3 than in Python 2.
Tip4:  \b  shortcut matches a zero-length substring. However, it only matches it at the beginning
           or end of a word. This is called the word boundary character shortcut. 

"""
print(re.search(r'[\bcorn\b]', 'corner'))  # returns matches the c
print(re.search(r'\bcorn\b', 'corn'))      # returns matches the corn , notice [ ] character class is missing
print(re.search(r'\bcorn\b', 'corner'))    # returns None


# It is worth noting that these shortcuts work both within character classes and outside of them. For
# example

print(re.search(r'\w', 'Python 3'))  # notice i removed [] character class and it matches the P
print(re.findall(r'\w', 'Python 3'))  # to make more clear when we use find all see below it find all the characters
# ['P', 'y', 't', 'h', 'o', 'n', '3']
# Note that the regular expression \w matches every character in the string except the space. The \w
# shortcut does include digits in the Python regular expression engine.








"""
The \w, \d, and \s shortcuts also include negation shortcuts: \W, \D, and \S. These shortcuts
match any character other than the characters in the shortcut. Note again that these still require a
character to be present. They do not match an empty string.

There is also a negation shortcut for \b, but it works slightly differently. Whereas \b matches a zerolength
substring at the beginning or end of a word, \B matches a zero-length substring that is not at
the beginning or end of a word. This essentially reverses the corn and corner example from earlier.
"""

print(re.search(r'corn\B', 'corner'))  # <_sre.SRE_Match object; span=(0, 4), match='corn'>
print(re.search(r'corn\B', 'corn'))    # None









"""
Beginning and End of String:
^ character designates the beginning of a string
$ character designates the end of a string

"""
print(re.search(r'^Python', 'This code is in Python'))     # return None,  as Python is not in beginning of string
print(re.search(r'[^P]ython', 'This code is in Python'))   # return None,  because when ^ is placed inside the []
                                                           # then it work like negitator
print(re.search(r'[^P]ython', 'This code is in Jython'))   # match='Jython'


print(re.search(r'^Python', 'Python 3'))                   # return match object Python as Python is at start of string
print(re.search(r'[^P]ython', 'Python 3'))                 # return None , as it negitates
print(re.search(r'[^P]ython', 'Jython 3'))                 # return match='Jython'
print(re.search(r'[^P]ython', 'I am Jython 3'))            # return match='Jython'

print(re.search(r'Python$', 'This code is in Python'))   # return match object Python as Python is at end of string
print(re.search(r'Python$', 'Python 3'))                 # return None,  as Python is not in end of string







"""
Any Character:
The . character is the final shortcut character. It stands in for any single character.
However, it only serves this role outside a bracketed character class.

Note that there is one character that the . does not match, which is newline (\n). It is possible to
make the . character match newline, however, which is discussed later in this chapter.
"""

# Notice when we put [.] it worked like a dot only and lost its power of matching any character
print(re.search(r"p[.]thon", "python 3"))  # None
print(re.search(r"p[.]thon", "p.thon 3"))  # match='p.thon'

# But now lets take it out of character class
print(re.search(r"p.thon", "python 3"))   #  match='python'
print(re.search(r"p.t..n", "python 3"))   #  match='python'





"""
Optional Characters
? character - ? means a character before ? will occur once or zero times.This makes a character may be optional.

English word honor is written as  "honour" in British Language.

"""
print(re.findall(r"hono[u?]r", "English word honor is written as  honour in British Language."))
# ['honour']
print(re.findall(r"honou?r", "English word honor is written as  honour in British Language."))
# ['honor', 'honour']
print(re.findall(r"hono[u]?r", "English word honor is written as  honour in British Language."))
# ['honor', 'honour']

# But careful when you use character class [u?] , Note the difference above




"""
Repetition
[\d]{3}-[\d]{4}
means 3 digit then hypengen and then again 4 digit

"""

print(re.search(r'[\d]{3}-[\d]{4}', 'Contact : Miss Jenny for Dating , 867-5309 ,  Jenny@many.com'))  # match='867-5309'

"""
Repetition Ranges
For example, consider credit card security codes. Credit cards issued in the United States contain a
special security code on the back, often called a “CVV code.” Most credit card brands use threedigit
security codes, which you can match with [\d]{3}. However, American Express uses fourdigit
security codes ([\d]{4}).

What if you want to be able to match both of these cases? Repetition ranges come in handy here.
The syntax here is {M,N}, where M is the lower bound and N is the upper bound.

[\d]{3,4}

Note: You might be tempted (based on using Python slices) to believe
that the upper bound is exclusive (and that you should use {3,5} instead). However, regular expressions
do not work this way.


"""
print(re.search(r'[\d]{3,4}', '0421'))   # match='0421'
print(re.search(r'[\d]{3,4}', '04218'))  # match='0421' but it  over matching
print(re.search(r'[\d]{3,4}', '615'))    # match='615'
"""
NOte:When given the choice to match three characters or four characters, where either is a valid match,
how does the regular expression engine decide? The answer is that, under most circumstances, the
regular expression engine is “greedy,” meaning that it will match as many characters as possible
for as long as it can. In this simple case, that means that if there are four digits, four digits will be
matched.
Occasionally, this behavior is undesirable. By placing a ? character immediately after the repetition
operator, it causes that repetition to be considered “lazy,” meaning that the engine will match as few
characters as possible to return a valid match.
"""
print(re.search(r'[\d]{3,4}', '615999999'))    # match='6159' but it  over matching  --> Greedy matching
print(re.search(r'[\d]{3,4}?', '615999999'))    # match='615' but it  over matching  ---> Lazy Matching
# Note that the ? in this situation does not serve to make the repeated segment optional. It simply
# means that, given the opportunity to match three or four digits, it will elect only to match three.


"""
Open-Ended Ranges
You also may encounter cases where there is no upper bound for the number of times that a token
may repeat. For example, consider a traditional street address. This usually starts with a number
(for the moment, hand-wave the exceptions and assert that they always do), but the number could
be any arbitrary length. There is nothing technically invalid about an eight-digit street number.
In these cases, you can leave off the upper bound, but retain the , character to designate that the
upper bound is ∞. For example, {1,} designates one or more occurrences with no upper bound.

"""
print(re.search(r'[\d]{3,}', '615999999'))  # match='615999999'
print(re.search(r'[\d]{1,}', '615999999'))  # match='615999999'
print(re.search(r'[\d]{1,}', 'amitsuneja007@gmail.com'))  # match='007'


"""
Shorthand
+ character in lieu of specifying {1,} (one or more).
* character in lieu of specifying {0,}

Note : Using + and * generally makes for a regular expression that is easier to read, and is the preferred
syntax in cases where they are applicable
"""
print(re.search(r'[\d]+', 'amitsuneja007@gmail.com'))  # match='007'
# Again i feel if i keep + inside brackets [+] it will loose its power.

str1 = 'Contact : Miss Jenny for Dating , +91-867-5309 ,  Jenny@many.com'
str2 = 'Contact : Miss Jenny for Dating , 867-5309 ,  Jenny@many.com'
str3 = 'Contact : Miss Jenny for Dating , 8675309 ,  Jenny@many.com'
str4 = 'Contact : Miss Jenny for Dating , 91-867-5309 ,  Jenny@many.com'
str5 = 'Contact : Miss Jenny for Dating , 0091-867-5309 ,  Jenny@many.com'
str6 = 'Contact : Miss Jenny for Dating , -867-5309 ,  Jenny@many.com'


match1 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str1)
match2 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str2)
match3 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str3)
match4 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str4)
match5 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str5)
match6 = re.search(r"[+?9]?[1]?-?[\d]{3}[-]?[\d]{4}", str6)

print(match1)
print(match2)
print(match3)
print(match4)
print(match5)
print(match6)

print("________________________________________________________________")

match = re.search(r'([\d]{3})[.-]([\d]{4})', '867-5309 / Jenny')
print(match.group())
print(match.groups())   # -> groups(0) which means all groups.
print(match.group(1))
print(match.group(2))

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '(213) 867-5309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '213-867-5309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '213.867.5309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '2138675309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '+1 (213) 867-5309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '1 (213) 867-5309')
print(match.groups(), match)

match = re.search(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})', '1-213-867-5309')
print(match.groups(), match)

# Group - 1
#
# (\+?1)?[ .-]?\(?
#
# (\+?1)?
#  + have a special meaning explained in above notes shorthand . But since my first character may be + sign
# so i want to treat + as a + synbol so i put \ in front of him
# now + may exist or may not thats why i put ? after + sign
# then i have a plan character 1 as i know USA code is +1 . Now some people may or may not write it hence i
#  put ? outside the bracket.
#
# [ .-]?
# i build a character class of . and - because i know people do separated number by either using any of them and since i
# not sure on its existence , I put ?
#
# \(?
# \ is used to escape ( . Now i now ( may or may not be present  then i used ?
#
#
# Group - 2
#
# ([\d]{3})\)?[ .-]?
#
# ([\d]{3})
# means any 3 digit number
#
# \)?
# \ is escape character then may or may not ) exist hence put ?
#
# [ .-]?
# i build a character class of . and - because i know people do separated number by either using any of them and since i
# not sure on its existence , I put ?
# Group 3 and 4 are simple.

"""
Named Groups:

Till now we know groups(0),groups(1) , Based on positional parameter of group , But we can name them.
The syntax for a named group is to add ?P<group_name> immediately after the opening ( character.


"""
match = re.search(r'(?P<first_three>[\d]{3})-(?P<last_four>[\d]{4})', '867-5309')
print(match.group())
print(match.group('first_three'))
print(match.group('last_four'))
print(match.groupdict())

# named groups are also still positional groups also.
print(match.group(1))
print(match.group(2))

# It is worth noting that groupdict, like groups, does not return the entire match; it only returns the
# subgroups. Also, if you have a mix of named groups and unnamed groups, the unnamed groups are
# not part of the dictionary returned by groupdict.

match = re.search(r'(?P<first_three>[\d]{3})-([\d]{4})', '867-5309')
print(match.groupdict())
# when groups is called, both groups are returned in the tuple.
# However, when groupdict is called, only the first_three group is included in the result.

"""
Referencing Existing Groups
OR
BackTracking 
"""

consider_string1 = "<foo>stuff</foo>"
consider_string2 = "<foo>stuff</bar>"

# We all know consider_string1 is right but consider_string2 is incorrect

print(re.search(r'<([\w_-]+)>stuff</([\w_-]+)>', consider_string1))
print(re.search(r'<([\w_-]+)>stuff</([\w_-]+)>', consider_string2))
# But my code is not able to find difference between foo and bar.

print(re.search(r'<([\w_-]+)>stuff</\1>', consider_string1))  # match='<foo>stuff</foo>
print(re.search(r'<([\w_-]+)>stuff</\1>', consider_string2))  # None
# Note : By reference to old group our issue is fixed. this is called BackTracking.


"""
Revision of Negation:
You can invert a character class (meaning that it will match any character other than those specified)
by beginning the character class with a ^ character.

"""
# Consider the regular expression n[^e]. This means the character n followed by any character that is not an e.
print(re.search(r'n[^e]', 'final'))  # return "na" match object
print(re.search(r'n[^e]', 'jasmine')) # return None , Here, the regular expression engine gets to the only n in the
                                      # string but cannot match the next character, because it is an e . Hence no match

# However, the regular expression also will not match against an n at the end of the string.
print(re.search(r'n[^e]', 'Python'))  # None

print("_____________________________________________")
"""
LOOKAHEAD:


"""
print(re.search(r'n(?!e)', 'final'))    # match='n'
print(re.search(r'n(?!e)', 'jasmine'))  # None
print(re.search(r'n(?!e)', 'Python'))   # match='n'

"""
These results are slightly different than when a negated character class was used. In the first
example, using the word final, the regular expression again matches, but the match is different.
While the negated character class made the a character part of the match, negative lookahead does
not, and the match comes back as just the n character.

The second result is the most similar. The n in jasmine matches the n character in the regular
expression. However, because the n is followed by an e, it is disqualifi ed, and the match fails.

The fi nal result is the most different, because this match actually succeeds, where it did not with a
negated character class. The regular expression engine matches the n in Python. It then reaches the
end of the string. Because that n is not followed by an e, the match succeeds and is returned.

It is worth noting that while this may look like group syntax, in this case, a group is not saved.

"""

match = re.search(r'n(?!e)', 'final')
print(match)
print(match.groups())


"""
The regular expression engine also supports a different kind of lookahead, called a positive
lookahead. This requires that the match be followed by the character or characters in question, but
nonetheless does not make those characters part of the match.
The syntax for positive lookahead simply replaces the ! character with =. Consider this regular
expression:

"""

print(re.search(r'n(?=e)', 'jasmine'))  # match='n'
print(re.search(r'n(?=e)', 'jasmin'))   # None

"""
In this case, the regular expression engine matches the n in the word jasmine. After doing so, it
verifies that the subsequent character is an e, as the regular expression requires. Because it is, the
match is complete and returned. As before, no group is created by the lookahead and Without the e, the match fails.
"""


"""
FLAGS:
Case Insensitivity
ASCII and Unicode
Dot Matching Newline

"""
print(re.search(r'python', 'PYTHON IS AWESOME', re.IGNORECASE))  # match='PYTHON'
# re.IGNORECASE (aliased to re.I)
# re.UNICODE (aliased to re.U) -> forces the regular expression engine to follow the Python 3 behavior.
# Note that if you try to use a byte string with re.U in Python 3, the parser will raise an exception.
# re.ASCII (aliased to re.A) flag forces the regular expression to follow the Python 2 behavior
# Note re.ASCII flag is not available in Python 2.
# re.DOTALL (aliased to re.S to match the terminology used in Perl and elsewhere) causes the . character to match
# newline characters in addition to all other characters.
# re.MULTILINE (aliased to re.M) causes the ^ and $ characters, which normally would only
# match against the beginning or end of the string (respectively), to instead match against the beginning
# or end of any line within the string.
# re.VERBOSE (aliased to re.X) allows for complicated regular expressions to be expressed in a more readable way
# re.DEBUG (not aliased) dumps some debugging information out to sys.stderr while compiling a regular expression.
# Multiple Flags can be used re.DOTALL |  re.S | re.M.

"""
SUBSTITUTION
re.sub - The regular expression engine is not limited to simply identifying whether a pattern exists within
a string. It is also capable of performing string replacement, returning a new string based on the
groups in the original one.
It takes three arguments: the regular expression, the replacement string, and the source string being searched. 
Only the actual match is replaced, so if there is no match, re.sub ends up being a no-op.
"""

"""
COMPILED REGULAR EXPRESSIONS
The re module contains a function, compile, which returns a compiled regular expression object,
which can then be reused.
The re module caches regular expressions that it compiles on the fl y, so in most situations, there is
no substantial performance advantage to using compile. It can be extremely useful for passing regular
expression objects around, however.

"""

regex = re.compile(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})')
print(regex.search('213-867-5309'))   # match='213-867-5309'

"""
Also, there is one other advantage to using re.compile. The search method of regular expression
objects actually allows for two additional arguments not available on re.search. These are the
starting and ending positions of the string to be searched against, enabling you to exempt some of
the string from consideration.

"""

regex = re.compile('[\d]+')
print(regex.search('1 mile is equal to 5280 feet.'))  # match='1'
print(regex.search('1 mile is equal to 5280 feet.', pos=2))  # match='5280'
