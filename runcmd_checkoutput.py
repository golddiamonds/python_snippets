#run a command line command and return its output
from subprocess import check_output

#using the "dir" command in windows here.
print check_output("dir", shell=True)