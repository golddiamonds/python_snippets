#returns a list of files and directories within the selected
#relative directory (depends on folder return_filesdirs.py is run from)

import os

#directory to check here
dir_name = ''

#return list of names
dir_list = os.listdir(dir_name)

#print them out
for item in dir_list:
	print item
