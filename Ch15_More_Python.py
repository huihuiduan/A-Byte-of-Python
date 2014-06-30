# Ch15_More_Python.py

# Special methods of __init__ and __del__
'''
__init__(self, ...) This method is called just before the newly created
object is returned for usage.

__del__(self) Called just before the object is destroyed

__str__(self) Called when we use the print statement with the
object or when str() is used.

__lt__(self, other) Called when the less than operator ( < ) is used.
Similarly, there are special methods for all the operators
(+, >, etc.)

__getitem__(self, key) Called when x[key] indexing operation is used.

__len__(self) Called when the built-in len() function is used
for the sequence object.
'''


# Single Statement Blocks
flag = True
if flag: print('Yes')




print('\nExample 15.1. Using List Comprehensions')
#!/usr/bin/python
# Filename: list_comprehension.py

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)





# Receiving Tuples and Lists in Functions

# There is a special way of receiving parameters to a function as a tuple or a dictionary using the * or **
# prefix respectively. This is useful when taking variable number of arguments in the function.

# Due to the * prefix on the args variable, all extra arguments passed to the function are stored in args
# as a tuple. If a ** prefix had been used instead, the extra parameters would be considered to be key/
# value pairs of a dictionary.

def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 4))
print(powersum(2, 10))




# A lambda statement is used to create new function objects and then return them at runtime.
print('Example 15.2. Using Lambda Forms')
#!/usr/bin/python
# Filename: lambda.py

def make_repeater(n):
    return lambda s: s * n

twice = make_repeater(2)

print(twice('word'))
print(twice(5))




# The exec and eval statements
exec('print("Hello World")')
print(eval('2*3'))

# The assert statement is used to assert that something is true.
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
# When the assert statement fails, an AssertionError is raised.
# assert len(mylist) >= 1




# The reprt function is used to obtain a canonical string representation of the object.
# Backticks (also called conversion or reverse quotes) do the same thing. Note that you will have eval(
#　repr(object)) == object most of the time.
i = []
i.append('item')
print(repr(i))
