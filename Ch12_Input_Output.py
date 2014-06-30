# Ch12_Input_Output.py


print('Example 12.1. Using files')
#!/usr/bin/python
# Filename: using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = open('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline().rstrip() # remove the \n at the end
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line, )# Notice comma to avoid automatic newline added by Python
f.close() # close the file







'''
Python provides a standard module called pickle using which you can store any Python object in a
file and then get it back later intact. This is called storing the object persistently.

There is another module called cPickle which functions exactly same as the pickle module except
that it is written in the C language and is (upto 1000 times) faster. You can use either of these modules,
although we will be using the cPickle module here. Remember though, that we refer to both these
modules as simply the pickle module.
'''

print('\nExample 12.2. Pickling and Unpickling')
#!/usr/bin/python
# Filename: pickling.py

try:
   import cPickle as p
except:
   import pickle as p
   
# import cPickle as p
# import pickle as p

shoplistfile = 'shoplist.data' # the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
p.dump(shoplist, f) # dump the object to a file, The output file needs to be opened in binary mode
f.close()

del shoplist # remove the shoplist

# Read back from the storage
f = open(shoplistfile, 'rb') # The input file needs to be opened in binary mode
storedlist = p.load(f)
print(storedlist)












