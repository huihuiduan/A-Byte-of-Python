# Ch11_OOP
# Class methods have only one specific difference from ordinary functions - they must have an extra first
# name that has to be added to the beginning of the parameter list, but you do do not give a value for this
# parameter when you call the method, Python will provide it. This particular variable refers to the object
# itself, and by convention, it is given the name self.

# Say you have a class called MyClass and an instance of this
# class called MyObject. When you call a method of this object as MyObject.method(arg1,
# arg2), this is automatically converted by Python into MyClass.method(MyObject, arg1,
# arg2 - this is what the special self is all about.



print('Example 11.1. Creating a Class')
#!/usr/bin/python
# Filename: simplestclass.py
class Person:
    pass # An empty block

p = Person()
print(p)



print('\nExample 11.2. Using Object Methods')
#!/usr/bin/python
# Filename: method.py
class Person:
    def sayHi(self):
        print('Hello, how are you?')

p = Person()
p.sayHi()
# This short example can also be written as Person().sayHi()




# The __init__ method is analogous to a constructor in C++, C# or Java.
print('\nExample 11.3. Using the __init__ method')
#!/usr/bin/python
# Filename: class_init.py
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)
        
p = Person('Swaroop')
p.sayHi()
# This short example can also be written as Person('Swaroop').sayHi()




# Class variables are shared in the sense that they are accessed by all objects (instances) of that class.
# There is only copy of the class variable and when any one object makes a change to a class variable, the
# change is reflected in all the other instances as well.

# Object variables are owned by each individual object/instance of the class. In this case, each object has
# its own copy of the field i.e. they are not shared and are not related in any way to the field by the samen
# name in a different instance of the same class. An example will make this easy to understand.

# Also, note that the __del__ method is analogous to the concept of a destructor.

print('\nExample 11.4. Using Class and Object Variables')
#!/usr/bin/python
# Filename: objvar.py
class Person:
    '''Represents a person.'''
    population = 0
    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print('(Initializing %s)' % self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
    def __del__(self):
        '''I am dying.'''
        print('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population)
    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print('Hi, my name is %s.' % self.name)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()
swaroop.sayHi()
swaroop.howMany()




print('\nExample 11.5. Using Inheritance')
#!/usr/bin/python
# Filename: inherit.py
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: %s)' % self.name)
    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"' % (self.name, self.age),)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "%d"' % self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print # prints a blank line
members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students



