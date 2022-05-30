import re

with open('import.txt', 'r') as file:
    for line in file:

        if re.findall(r'(?<=\s)([A-Z][a-z]{2,}\b)', line):
            fname, lname = re.findall(r'(?<=\s)([A-Z][a-z]{2,}\b)', line)
        elif re.findall(r'(?<=\s)([A-Z][a-z0-9]{3,})', line):
            address, = re.findall(r'(?<=\s)([A-Z][a-z0-9]{3,})', line)
        elif re.findall(r"([a-zA-Z0-9_]+)(@)([a-zA-Z]+)(.)(com|net|org|edu)", line):
            email = ''.join((re.findall(r"([a-zA-Z0-9_]+)(@)([a-zA-Z]+)(.)(com|net|org|edu)", line))[0])
        elif re.findall(r"([a-zA-Z0-9]+)|\d+", line):
            print(re.findall(r"(?<=\s)^([A-z!@# _]+\d+)\|\d+", line))
