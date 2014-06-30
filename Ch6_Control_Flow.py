# Ch6_Control_Flow.py


# Example 6.1. Using the if statement
#!/usr/bin/python
# Filename: if.py
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    print('Congratulations, you guessed it.') # New block starts here
    print("(but you do not win any prizes!)") # New block ends here
elif guess < number:
    print('No, it is a little higher than that') # Another block
# You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
# you must have guess > number to reach here
print('Done')


# Example 6.2. Using the while statement
#!/usr/bin/python
# Filename: while.py
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False # this causes the while loop to stop
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done')


# Example 6.3. Using the for statement
#!/usr/bin/python
# Filename: for.py
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

# The break statement is used to break out of a loop statement i.e. stop the execution of a looping statement,
# even if the loop condition has not become False or the sequence of items has been completely
# iterated over.
# Example 6.4. Using the break statement
#!/usr/bin/python
# Filename: break.py
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')

# The continue statement is used to tell Python to skip the rest of the statements in the current loop
# block and to continue to the next iteration of the loop.
# Example 6.5. Using the continue statement

#!/usr/bin/python
# Filename: continue.py
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here...



