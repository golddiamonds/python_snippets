#checks to see if a directory exists, if it doesn't then it creates that directory.
#this has the potential for a race condition between the time it checks the
#directory to the time it creates the directory (the dir could be created...
#causing an error). But in programs and situations where that is not a concern
#this works really well.

import os

#directory name here
dir_name = ''

#check for existence in current directory
if not os.path.exists(dir_name):
	#if it doesn't exist, create it
	os.makedirs(dir_name)
