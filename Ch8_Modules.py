# Ch8_Modules.py
# A module is basically a file containing all your functions and variables that you have
# defined. To reuse the module in other programs, the filename of the module must have a .py extension.


# When Python executes the import sys statement, it looks for the sys.py module in one of the directores
# listed in its sys.path variable.
# Example 8.1. Using the sys module
#!/usr/bin/python
# Filename: using_sys.py
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')


# Importing a module is a relatively costly affair, so Python does some tricks to make it faster. One way is
# to create byte-compiled files with the extension .pyc which is related to the intermediate form that Python
# transforms the program into


# Example 8.2. Using a module's __name__
#!/usr/bin/python
# Filename: using_name.py
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

# import Ch8_Modules
# This will print 'I am being imported from another module'


# Example 8.3. How to create your own module

#!/usr/bin/python
# Filename: Ch8_Modules.py
def sayhi():
    print('Hi, this is Ch8_Modules speaking.')
version = '0.1'
# End of Ch8_Modules.py

# Use the model in another program????
'''
import Ch8_Modules
Ch8_Modules.sayhi()
print('Version', Ch8_Modules.version)
'''


'''
# from import example
#!/usr/bin/python
# Filename: mymodule_demo2.py
from Ch8_Modules import sayhi, version
# Alternative:
# from mymodule import *
sayhi()
print('Version', version)
'''

# dir() function, it returns the list of the names defined in that
# module. When no argument is applied to it, it returns the list of names defined in the current module.

# Example 8.4. Using the dir function
import sys
dir(sys)
