import re
print(re.search(r'[Pp]ython', 'Python 3'))   # P is CAPITAL

match = re.search(r'([Pp]y)([Tt]h)(o[nf])', 'PyThof 3')
print(match.groups())