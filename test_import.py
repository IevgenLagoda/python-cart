import re

with open('import.txt', 'r') as file:
    for line in file:

        if re.findall(r'(?<=\s)([A-Z][a-z]{2,}\b)', line):
            fname, lname = re.findall(r'(?<=\s)([A-Z][a-z]{2,}\b)', line)

            #print(fname, lname)
        elif re.findall(r'(?<=\s)([A-Z][a-z]{3,})', line):
            print(re.findall(r'(?<=\s)([A-Z][a-z]{3,})', line))
            address = re.findall(r'\b[A-z][a-z][0-9]{3,}\b', line)
            #print(address)
