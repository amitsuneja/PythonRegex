import re

data_file = 'names.txt'

with open(data_file, 'r', encoding="utf-8") as myfile:
	data_dump = myfile.read()


email_ids = re.findall(r"[\w+._\d]+@[\w._]+", data_dump)
print(email_ids)
print(len(email_ids))

