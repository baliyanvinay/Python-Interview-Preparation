# Python Interview Preparation

## 1. Explain 'Everything in Python is an object'.
What's an object? An object in a object-oriented programming language is an entity that contains data along with some methods for operations related to that data. <br>
Everything from numbers, lists, strings, functions and classes are python objects. 
```python
>>> a = 10.5
>>> a.is_integer() # Float type has is_integer() method cause a is an object of float class
False
>>> type(a)
<class 'float'>
>>> def func()
....    pass
>>> type(func)
<class 'function'>
>>> # like functions, classes are also objects of 'type' class
```
Look at the below example
```python
>>> var = 'Tom' # Object 'Tom' is created in memory and name 'var' is binded to it. 
>>> var = 'Harry' # Another object is created however note that name 'var' is now binded to 'Harry' but 'Tom' is still somewhere in memory and is unaffected.
```
Ref: [Nina Zakharenko - Memory Management in Python - The Basics - PyCon 2016](https://www.youtube.com/watch?v=F6u5rhUQ6dU)

## 2. What is mutable and immutable objects/data types in Python?
Mutation generally refers to 'change'. So when we say that an object is mutable or immutable we meant to say that the value of object can/cannot change. <br>
When an object is created in Python, it is assigned a type and an id. An object/data type is mutable if with the same id, the value of the object changes after the object is created. 
##
<b>Mutable objects in Python</b>
-- Objects that can change after creation. Lists, byte arrays, sets, and dictionaries.
```python
>>> list_var = [17, 10]
>>> list_var
[17, 10]
>>> id(list_var)
2289772854208
>>> list_var += [17]
>>> list_var
[17, 10, 17]
>>> id(list_var) # ID of the object didn't change.
2289772854208
```

## 
<b>Immutable objects in Python</b>
-- Numeric data types, strings, bytes, frozen sets, and tuples.
```python
>>> # Example of tuples
>>> tuple_var = (17,)
>>> tuple_var
(17,)
>>> id(tuple_var)
1753146091504
>>> tuple_var += (10,)
>>> tuple_var
(17,10)
>>> id(tuple_var) # ID changes when made changes in object.
1753153466880
```

## 3. What is the difference between list and tuples in Python?

| Parameter | List | Tuples |
| :-------------:|:-------------:| :-------------:| 
|  Syntax   | Square brackets or list keyword | Round brackets/parenthesis or tuple keyword |
| Nature    | Mutable  | Immutable |
| Item Assignment | Possible  | Not Possible |
| Reusablity | Copied  | Not Copied |
| Performance | Relatively slower  | Relatively faster |
| Memory | Large-Extra than the element size | Fixed to element size |

### Memory Allocation of Tuple and List
Tuple does not allot any extra memory during construction because it will be immutable so does not have to worry about addition of elements. 
```python
>>> tuple_var = tuple()
>>> tuple_var.__sizeof__() # take 24 bytes for empty tuple
24
>>> tuple_var = (1,2) # additional 8 bytes for each integer element
>>> tuple_var.__sizeof__()
40
```
List over-allocates memory otherwise list.append would be an O(n) operation. 
```python
>>> list_var = list()
>>> list_var.__sizeof__() # take 40 bytes for empty list
40
>>> list_var.append(1)
>>> list_var.__sizeof__() # append operation allots extra memory size considering future appends
72
>>> list_var
[1]
>>> list_var.append(2)
>>> list_var.__sizeof__() # size remains same since list has space available
72
>>> list_var
[1,2]
```
### Reusablity
Tuple literally assigns the same object to the new variable while list basically copies all the elements of the existing list.
```python
>>> # List vs Tuples | Reused vs. Copied
>>> old_list = [1,2]
>>> old_list.append(3)
>>> old_list
[1, 2, 3]
>>> id(old_list) 
2594206915456
>>> old_list.__sizeof__()
88

>>> # Copying list
>>> new_list = list(old_list)
>>> new_list
[1, 2, 3]
>>> id(new_list) # new id so new list is created
2594207110976
>>> new_list.__sizeof__() # size is also not same as old_list
64

>>> Tuple Copy
>>> old_tuple = (1,2)
>>> id(old_tuple)
2594206778048
>>> old_tuple.__sizeof__()
40
>>> new_tuple = tuple(old_tuple)
>>> id(new_tuple) # same id as old_tuple
2594206778048
>>> new_tuple.__sizeof__() # also same size as old_tuple since it is refering to old_tuple
40
```

### Performance-Speed
Tuples and List takes almost same time in indexing, but for construction, tuple destroys list. See example, 'List vs Tuple'. 

## 4. How is memory managed in Python?
Unlike other programming languages, python stores references to an object after it is created. For example, an integer object 17 might have two names(variables are called names in python) a and b. The memory manager in python keeps track of the reference count of each object, this would be 2 for object 17. Once the object reference count reaches 0, object is removed from memory. <br>
The reference count 
- increases if an object is assigned a new name or is placed in a container, like tuple or dictionary.
- decreases when the object's reference goes out of scope or when name is assigned to another object. 
Python's garbage collector handles the job of removing objects & a programmer need not to worry about allocating/de-allocating memory like it is done in C.
```python
>>> import sys
>>> sys.getrefcount(17)
>>> 11
>>> a = 17
>>> b = 17
>>> a is b
>>> True
>>> sys.getrefcount(17)
>>> 13 # addition of two
```

## 5. Explain exception handling in Python.
Exception handling is the way by which a programmer can control an error within the program without breaking out the flow of execution. 
```python
try:
    # Part which might cause an error
except TypeError:
    # What happens when error occurs | In this case what happens what a TypeError occurs
else:
    # what happens if there is no exception | Optional
finally:
    # Executed after try and except| always executed | Optional
```
Examples :- TypeError, ValueError, ImportError, KeyError, IndexError, NameError, PermissionError, EOFError, ZeroDivisionError, StopIteration

##  6. Explain some changes in Python 3.8
Positional arguements representation
```python
def sum(a,b,/,c=10):
    return a+b+c
sum(10,12,c=12)
```
F String can also do operations
```python
a,b = 10, 12
f"Sum of a and b is {a+b}"
f"Value of c is {(c := a+b)}"
```

## 7. Explain Python Design Patterns. 
Ref: https://www.youtube.com/watch?v=o1FZ_Bd4DSM

## 8. How would you load large data file in Python?
The best way is to load data in chunks, Pandas provides option to define chunk size while loading any file. 
```python
for chunk in pd.read_csv(file.csv, chunksize=1000):
    process(chunk)
    
pd.read_csv('file.csv', sep='\t', iterator=True, chunksize=1000)
```
Another way is to use context manager.
```python
with open("log.txt") as infile:
    for line in infile:
        do_something_with(line)
```

## 9. Explain Generators and use case of it.
A function or method which uses the yield statement is called a generator function. Such a function, when called, always returns an iterator object which can be used to execute the body of the function: calling the iterator’s iterator.\__next__()method will cause the function to execute until it provides a value using the yield statement. <br>
When the function executes a return statement or falls off the end, a StopIteration exception is raised and the iterator will have reached the end of the set of values to be returned.
#### Use Case
Generators are good for calculating large sets of results where you don't know if you are going to need all results, or where you don't want to allocate the memory for all results at the same time.

```python
# Search function as generator, effective for returning some set as result with functionality like 'Load 10 more items'
def search_result(keyword):
    while keyword in dataset:
        yield matched_data

search_object = search_result('keyword')
# type(search_function)  --> <class 'generator'>

search_object.__next__()
```
Example: https://github.com/baliyanvinay/Python-Advanced/blob/main/Generator.py

## 10. Is there a sequence in defining exceptions in except block for exception handling?
Yes can be defined in a tuple. From left to right will be executed based on the exception raised. 
```python
try:
    pass
except (TypeError, IndexError, RuntimeError) as error:
    pass
```

## 11. Explain Closures in Python
A closure is a functionality in Python where some data is memorized in the memory for lazy execution. Decorators heavily rely on the concept of closure. <br>
To create a closure in python:-
1. There must be a nested function(function within a enclosing/outer function)
2. The nested function must refer to a value defined in the enclosing function
3. The enclosing function must return(not call it) the nested function.
```python
def enclosing_function(defined_value):
    def nested_function():
        return defined_value+some_operation
    return nested_function

closure_function = enclosing_function(20)
closure_function() # returns 20+some_operation
```
Objects are data with methods attached, closures are functions with data attached.

## 12. How to make a chain of function decorators?
```python
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@make_bold
@make_italic
def index():
    return "hello world"

print(index()) 
## returns "<b><i>hello world</i></b>"

```

## 13. Three different ways to fetch every 3rd item of a list
Using index jump
```python
>>> example_list = [0,1,2,3,4,5,6]
>>> example_list = [::3] # returns [0,3,6]
```
Using list comphrehension
```python
>>> [x for x in example_list if example_list.index(x)%3==0]
>>> [0,3,6]
```
Using while loop
```python
i = 0
while i < len(example_list):
    print(example_list[i])
    i += 3
```

## 14. What is MRO in Python? How does it work?
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes. 
```python
class A:
    def process(self):
        print('A')
        
class B(A):
    pass
    
class C(A):
    def process(self):
        print('C')

class D(B,C):
    pass
    
obj = D()
obj.process()
# D -> B -> C -> A -> object 
```
Note: a class can't be called before its superclass in resolving MRO. Super Class has to be called after derived class

## 15. What is monkey patching? How to use it in Python?
## 16. What is the difference between staticmethod and classmethod?
| Parameter | Class Method | Static Method |
| :-------------:|:-------------:| :-------------:|
| Decorator | @classmethod | @staticmethod |
| Use Case| More widely used as a factory method to class | Acts as utility functions |
| Scope | Bound to the classs and not objects | Also bound to class and not objects |
| Behaviour | Can modify the state of the class | Can't access class state |
| Parameter | Takes cls as first parameter | No specific parameter |
```python
class Circle:
    no_of_circles = 0
    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles += 1
        
    @staticmethod
    def square(num):
        return num**2
    
    @classmethod
    def getCircleCount(cls):
        return cls.no_of_circles
```

## 17. What is the purpose of the single underscore “_” variable in Python?
Python automatically stores the value of last expression in interpreter in single underscore. 
```python
>>> 78 + 89
167
>>> _
167
```
Single underscore used in unpacking to ignore value(s). 
```python
>>> a, _, b = (1, 12, 2)
>>> a, *_, b = (1, 12, 13, 14, 15, 16, 2) # only want first and last value
>>> a, *x, b = (1, 12, 13, 14, 15, 16, 2) # note that any other name can also be used
>>> _ # returns a list of elements
[12, 13, 14, 15, 16]
```
It is most commonly used in loops where we are not interested in the value returned by the iterator.
```python
for _ in range(5):
    print('Some operations')
```
Note that it is entirely the convention to use single underscore in all these ways to avoid having defined extra variable for such operations.

## 18. What's the difference between a Python module and a Python package?
#### Module
The module is a Python file that contains collections of functions and global variables and with having a .py extension file.
### Package
The package is a directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package. 

## 19. What is a global interpreter lock (GIL)?
Ref: https://www.geeksforgeeks.org/what-is-the-python-global-interpreter-lock-gil/

## 20. Which is faster, list comprehension or for loop?
## 21. Explain Singleton class and its uses?
Refer to [Python Advanced : Design Patterns](https://github.com/baliyanvinay/Python-Advanced/tree/main/Design%20Patterns)

## 22. Explain Meta Classes in Python.
In Python everything is an object, even a class is an object. As a result, a class also must have a type. All classes in Python are of 'type' type. Even the class of 'type' is 'type'. So 'type' is the meta class in Python and to create custom meta class, you would need to inherit from 'type'.<br>
### Use Case of Meta Class
A meta class is the class of a class. A class is an instance of a metaclass. A metaclass is most commonly used as a class-factory. When you create an object by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass.<br>
```python
>>> type(17) # <class 'int'>
>>> type(int) # <class 'type'>
>>> str.__class__ # <class 'type'>
>>> type.__class__ # <class 'type'>
```
### Meta Class call
The metaclass is called with the 
- name: name of the class, 
- bases: tuple of the parent class (for inheritance, can be empty) and 
- attributes: dictionary containing attributes names and values.
```python
def init(self, make):
    self.make = make

# type(name, bases, attrs) 
>>> Car = type('Car', (object,), {'__init__': init, '__repr__': lambda self: self.make,  'wheels': 4})
>>> seltos = Car('Kia')
>>> seltos # Kia
```
Ref: [Stack Overflow : Meta Classes](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)

## 23. Best way to concatenate n number of strings together into one.
## 24. Explain briefly about map() and lambda() functions.
### map(function, iterable)
Map function returns an iterator that applies function to every item in the iterable. In case multiple iterables are passed, the iterator stops when the shortest iterable is exhausted.
```python
def custom_power(x, y):
    return x**y

values = [1,2,3,4]
powers = [2,1,2] 
map_iterator = map(custom_power, values, powers) # will skip the power of 4
print(list(map_iterator)) # [1,2,9]
```
### lambda parameters: expression
Lambda expression yields an anonymous function object. Note that functions created with lambda expressions cannot contain statements or annotations. For example, can't assign variables in lambda definition.
```python
>>> list(map(lambda x: x+10, [1,2,3])) # [11,12,13]
>>> func =  lambda x: x+10 # <function <lambda> at 0x7fdb99e9c310>
>>> func(25) # returns 35
```

## 25. Explain Abstract Classes and its uses.
## 26. Explain object creation process in detail. Which method is called first?
When an object of a class is created or a class is instantiated, the \__new__() method of class is called. This particular method is resposible for returning a new class object. It can be overriden to implement object creational restrictions on class. <br>
- The constructor of the class is \__new__() and 
- the initializer of the class is \__init__(). <br>
Initializer is called right after the constructor, if the constructor has not returned a class object, the initializer call is useless. <br>
Note that the reason \__init__() could use class object(self) to initialize is because when the code flow reaches \__init__() the object of the class is already created. 

## 27. Difference between a class variable and instance variable.
| Parameter | Class Variable | Instance Variable |
| :-------------:|:-------------:| :-------------:|
| Declaration | Inside class definition but outside of any instance methods | Inside constructor method i.e., \__init__ |
| Scope | Shared across all objects | Tied to the object instance |
| Behaviour | Any change is reflected across all instances | Change limited to instances only |
| Access | cls.variable_name | self.variable_name |

```python
class Car:
    total_cars, wheels = 0, 4
    def __init__(self, engine_power):
        self.engine_power =  engine_power
        Car.total_cars += 1 # incremented anytime a new car is added. 
        
kia_sonet = Car(120)
print(kia_sonet.wheels) # returns 4
kia_sonet.wheels += 1 # extra wheel
print(kia_sonet.wheels) # returns 5

print(Car.total_cars) # returns 1
print(Car.wheels) # returns 4 not 5
Car.wheel = 6 # two extra wheels

print(kia_sonet.wheels) # returns 6 now
```
Example: https://github.com/baliyanvinay/Python-Advanced/blob/main/Class%20Variables.py

## 28. Explain the concept behind dictionary in Python
- A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.
- A key can appear in a dictionary only once. Duplicate keys are not allowed
- Using a key twice in initial dict definition will override the first entry
- Key must be of a type that is immutable. Values can be anything

```python
>>> dict_sample_01 = {1: 12, 2: 14, 1: 16}
>>> dict_sample_02 # {1: 16, 2: 14}
>>> dict_sample_02 = dict.fromkeys('123')
>>> dict_sample_02 # {'1': None, '2': None, '3': None}
```

## 29. Difference between an expression and a statement in Python
A statement is a complete line of code that performs some action, while an expression is any section of the code that evaluates to a value. An expression is also a statement. Note that lambda function in Python only accepts expressions. 

## 30. Explain threading in Python
## 31. Can set have lists as elements?
## 32. Is method overloading possible in Python?
## 33. Explain multiple inheritance in Python.
## 34. Explain method resolution order for multiple inheritance
## 35. What can be used as keys in dictionary?
## 36. Explain shallow and deep copy in Python

## Coding Question
```python
# Transpose a square matrix of n rows and columns
# Write a function that will place even elements of an array at even indexes and odd at odd indexes. 
# Write a function that checks if an array is a subsequence of first array
# Write a function that unzips nested dicts into expanded dicts.
# What is the output of (0,1,2,3,(4,5,6),7,8)[::3]
# Output of a=[[]]*5, a[0].append(1)
```
