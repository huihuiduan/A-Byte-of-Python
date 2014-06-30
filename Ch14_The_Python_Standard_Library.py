# Ch14_The_Python_Standard_Library.py

print('Example 14.1. Using sys.argv')
#!/usr/bin/python
# Filename: cat.py

import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = open(filename, 'r')
    while True:
        line = f.readline().rstrip()
        if len(line) == 0:
            break
        print(line, ) # notice comma
    f.close()
    
# Script starts from here
if len(sys.argv) < 2:
    print('No action specified.')
    sys.exit()
    
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number
--help : Display this help''')
    else:
        print('Unknown option.')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)








import sys
help(sys)
dir(sys)
help(sys.path)



import os
# specifies which platform you are using, such as 'nt' for Windows and
# 'posix' for Linux/Unix users.
os.name

# gets the current working directory
os.getcwd()

# get and set environment variables
os.getenv()
os.putenv()

# returns the name of all files and directories in the specified directory
os.listdir()

# delete a file
os.remove()

# run a shell command
os.system()

# gives the line terminator used in the current platform. For example, Windows
# uses '\r\n', Linux uses '\n' and Mac uses '\r'.
os.linesep

os.path.split('/home/swaroop/byte/code/poem.txt')

os.path.isfile()
os.path.isdir()
os.path.exists()
help(os)


