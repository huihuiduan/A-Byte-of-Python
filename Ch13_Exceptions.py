# Ch13_Exceptions.py

print('\nExample 13.1. Handling Exceptions')
#!/usr/bin/python
# Filename: try_except.py

import sys

try:
    s = input('Enter something --> ') # Enter Ctrl + d
except EOFError:
    print('\nWhy did you do an EOF on me?')
    # sys.exit() # exit the program
except:
    print('\nSome error/exception occurred.')
    # here, we are not exiting the program
print('Done')



'''
You can raise exceptions using the raise statement. You also have to specify the name of the error/
exception and the exception object that is to be thrown along with the exception. The error or exception
that you can arise should be class which directly or indirectly is a derived class of the Error or Exception
class respectively.
'''
print('\nExample 13.2. How to Raise Exceptions')
#!/usr/bin/python
# Filename: raising.py

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
try:
    s = input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
        # Other work can continue as usual here
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x: # , x in python 2.6
    print('ShortInputException: The input was of length %d, \
    was expecting at least %d' % (x.length, x.atleast))
else:
    print('No exception was raised.')




'''
What if you were reading a file and you wanted to close the file whether or not an exception was raised?
This can be done using the finally block. Note that you can use an except clause along with a finally
block for the same corresponding try block. You will have to embed one within another if you
want to use both.
'''
print('\nExample 13.3. Using Finally')
#!/usr/bin/python
# Filename: finally.py

import time

try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline().strip()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line,)
finally:
    f.close()
    print('Cleaning up...closed the file')




'''
Python Strip, lstrip, rstrip
http://www.youtube.com/watch?v=S1rO8ikU7YM
'''
x = '   korea   '
print(x)
x.lstrip()
print(x)
x.rstrip()
print(x)
x.strip()
print(x)
x = x.strip()
print(x)




