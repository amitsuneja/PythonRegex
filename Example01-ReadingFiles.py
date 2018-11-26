import re


data_file = 'names.txt'
with open(data_file, 'r', encoding="utf-8") as myfile:
	for line in myfile:
		# print(line)
		pass

with open(data_file, 'r', encoding="utf-8") as myfile:
	data_list = myfile.readlines()

with open(data_file, 'r', encoding="utf-8") as myfile:
	data_dump = myfile.read()

"""
remember data_dump will ast as a one string
"""
print(re.match('(Love)', data_dump))  # match='Love'
print(re.match('(Kenneth)', data_dump))  # None , because match will only check at beginning of line
print(re.match('(Doctor)', data_dump))   # None , because match will only check at beginning of line

print(re.search('(Kenneth)', data_dump))  # match='Kenneth'

last_name = r'Love'
first_name = r'Kenneth'
print(re.search(last_name, data_dump))  # match='Love'
print(re.search(first_name, data_dump))  # match='Kenneth'






