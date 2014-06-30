# Ch7_Functions.py


# Example 7.1. Defining a function
#!/usr/bin/python
# Filename: function1.py
def sayHello():
    print('Hello World!') # block belonging to the function
# End of function
sayHello() # call the function



# Example 7.2. Using Function Parameters
#!/usr/bin/python
# Filename: func_param.py
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')
printMax(3, 4) # directly give literal values
x = 5
y = 7
printMax(x, y) # give variables as arguments



# Example 7.3. Using Local Variables
#!/usr/bin/python
# Filename: func_local.py
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
x = 50
func(x)
print('x is still', x)



# Example 7.4. Using the global statement
#!/usr/bin/python
# Filename: func_global.py
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
x = 50
func()
print('Value of x is', x)


# Example 7.5. Using Default Argument Values
#!/usr/bin/python
# Filename: func_default.py
def say(message, times = 1):
    print(message * times)
say('Hello')
say('World', 5)



# Example 7.6. Using Keyword Arguments
#!/usr/bin/python
# Filename: func_key.py
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)



# Example 7.7. Using the literal statement
#!/usr/bin/python
# Filename: func_return.py
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print(maximum(2, 3))


# DocStrings
# Python has a nifty feature called documentation strings which is usually referred to by its shorter name
# docstrings. DocStrings are an important tool that you should make use of since it helps to document the
# program better and makes it more easy to understand. Amazingly, we can even get back the docstring
# from, say a function, when the program is actually running!

# Example 7.8. Using DocStrings
#!/usr/bin/python
# Filename: func_doc.py
def printMax(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
printMax(3, 5)
print(printMax.__doc__)






