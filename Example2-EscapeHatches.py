import re

data_file = 'names.txt'

with open(data_file, 'r', encoding="utf-8") as myfile:
	data_dump = myfile.read()

# print(data_dump)
print("___________________________________")
print(re.findall(r"(\+\d[\-\s])", data_dump))
print("___________________________________")
print(re.findall(r"(\+\d[\s\-])?(\(?\d{3}\)?)", data_dump))
print("___________________________________")
print(re.findall(r"(\+\d[\s\-])?(\(?\d{3}\)?)([\s\-.]\d{3})", data_dump))
print("___________________________________")
print(re.findall(r"(\+\d[\s\-])?(\(?\d{3}\)?)([\s\-.]\d{3})([\s.-]?\d{3,6})", data_dump))
print(len(re.findall(r"(\+\d[\s\-])?(\(?\d{3}\)?)([\s\-.]\d{3})([\s.-]?\d{3,6})", data_dump)))
