#Everyone should know how to load a file.
#Then read it line by line.

f = open("file.txt")

for line in f:
	print line, #the comma prevents newlines from being added to print statement