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
##
<b>Mutable objects and functon arguments</b>
```python
def sample_func(sample_arg):
    sample_agr.append(10)
    # No need to return the obj since it is utilizing the same memory block

sample_list = [7, 8, 9]
sample_func(sample_list)
print(sample_list) # [7, 8, 9, 10]
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

Note: It is not required for tuples to have parenthesis, one can also define tuple ```python a = 2, 3, 4 ```

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
When the function executes a return statement or falls off the end, a StopIteration exception is raised and the iterator will have reached the end of the set of values to be returned. Note that a generator can have n numbers of yield statements
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
Note: You can only iterate over a generator once, if you try to loop over it second time it will return nothing. Generators also do not store all the values in memory, they generate the values on the fly
```python
mygenerator = (x*x for x in range(3))
```
When you call a generator function, the code you have written in the function body does not run. The function only returns the generator object.
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
List comprehensions are generally faster than 'a for loop' because of the implementation of both. One key difference is that 'for loop' generally rounds up more than one statement/operation as compared to 'list comprehension' which has to perform single operation on all the elements. For example, creating a list or update in an existing list is faster when done using list comprehension.

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
The best way of appending a string to a string variable is to use + or +=. This is because it's readable and fast. However in most of the codebases we see use of append and join when joining strings together, this is done for readablity and cleaner code. Sometimes it is more important to have code readablity to actually understand the operation.
```python
first_name = 'Max '
last_name = 'Verstappen'
full_name = first_name + last_name
# using join string method
full_name = ''.join( (first_name, last_name) ) # takes in tuple of string in case of multiple values
```

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
>>> # lambda [parameter list] : expression
>>> list(map(lambda x: x+10, [1,2,3])) # [11,12,13]
>>> func =  lambda x: x+10 # <function <lambda> at 0x7fdb99e9c310>
>>> func(25) # returns 35
>>> lambda : 'hello' # with no parameter
```

## 25. Explain Abstract Classes and its uses.
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. Or in more general terms, a class which contains one or more abstract methods is called an abstract class.<br>
By default Python does not provide abstract class, ABC module of Python can be used to define an abstract class. 
### Abstract Method
Abstract method is a method that has a declaration but does not have an implementation. This ensures that any class built from this class will have to implement the method. 
```python
from abc import ABC, abstractmethod
class DB_PLugin(ABC):
    @abstractmethod
    def add_source(self):
        pass
```

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
You can't add a list to a set because lists are mutable, meaning that you can change the contents of the list after adding it to the set. You can however add tuples to the set, because you cannot change the contents of a tuple. <br>
The objects have to be hashable so that finding, adding and removing elements can be done faster than looking at each individual element every time you perform these operations. <br>
Some unhashable datatypes:
- list: use tuple instead
- set: use frozenset instead

## 32. Is method overloading possible in Python?
Yes method overloading is possible in Python. It can be achived using different number of arguments. 
```python
def increment(value, by=1):
   return value+by

# calling function
increment(5) # returns 6
increment(5, 2) # return 7
```

## 33. Explain inheritance in Python.
![Inheritance in Python](https://github.com/baliyanvinay/Python-Interview-Preparation/blob/main/Inheritance.png)

## 34. Explain method resolution order for multiple inheritance
## 35. What can be used as keys in dictionary?
Any immutable object type can be used as dictionary key even functions and classes can also be used as dictionary keys. 
#### Why can't list or another dict(mutable object) be used as key in dictionary?
Dict implementation reduces the average complexity of dictionary lookups to O(1) by requiring that key objects provide a "hash" function. Such a hash function takes the information in a key object and uses it to produce an integer, called a hash value. This hash value is then used to determine which "bucket" this (key, value) pair should be placed into. Mutuable objects like list or dict cannot provide a valid /__hash__ method.

## 36. Explain shallow and deep copy in Python
For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. <br>
Python follows a pattern of compiling the original source to byte codes, then interpreting the byte codes on a virtual machine. The .pyc file generated contains byte code. 
```python
>>> import copy
>>> sample_1 = [1,2,3]
>>> id(sample_1)
139865052152768
>>> sample_2 = sample_1
>>> id(sample_2)
139865052152768
>>> sample_3 = copy.copy(sample_1)
>>> id(sample_3)
139865052236736
```
- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Ref: [Python Docs Copy](https://docs.python.org/3/library/copy.html)

## 37. Why Python generates a .pyc file even when it is an interpreted language?
.pyc files are created by the Python interpreter when a .py file is imported, and they contain the "compiled bytecode" of the imported module/program, the idea being that the "translation" from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. But it's still interpreted.

## 38. How private varibles are declared in Python?
Python does not have anything called private member however by convention two underscore before a variable or function makes it private. 
```python
class XSpecial:
    normal_var = 10
    __private_var = 17

>>> special_obj = XSpecial()
>>> special_obj.normal_var
>>> special_obj.__private_var # AttributeError
```
## 39. Difference between an array and list
| List | Array | 
| :-------------:|:-------------:|
| Can contain elements of different data types | Contains homogeneous elements only i.e. same data type |
| No need to import | Need to import via numpy or array |
| Preferred for short sequence of data items | Preferred for large sequence of data items i.e., data analysis |
| Can't perform airthmetic operations on whole list | Great for airthmetic operations |

## 40. What is an iterator? How is iterator is different from a generator? 
An iterator is an object that implements /__next__, which is expected to return the next element of the iterable object, and raise a StopIteration exception when no more elements are available.
### Differnce between iterator and generator
| Iterator | Generator | 
| :-------------:|:-------------:|
| Class is used to implement an iterator | Function is used to implement a generator |
| Iterator uses iter() and next() functions | Generator uses yield keyword |
| Every iterator is not a generator | Every generator is an iterator |
| Saves the states of local variables every time ‘yield’ pauses execution | An iterator does not make use of local variables |
| Memory efficient | More memory allocated than iterator |

## 41. How do you define a dict where several keys has same value?
```python
products = {}
products.update(
    dict.keys(['Apple','Mango','Oranges'], 20)
)
products.update(
    dict.keys(['Pizza','Kind Pizza','Bad Pizza'], 30)
)
```
## 42. What are different types of namespaces in Python?
Namespace is a way to implement scope. In Python, each package, module, class, function and method function owns a "namespace" in which variable names are resolved. Plus there's a global namespace that's used if the name isn't in the local namespace.<br>
Each variable name is checked in the local namespace (the body of the function, the module, etc.), and then checked in the global namespace.
### Types of Namespaces
- <b>Local Namespace: </b>The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. 
- <b>Global Namespace: </b>The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
- <b>Built-in Namespace: </b>The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted.

## 43. How can you access attribute of parent class bypassing the attribute with the same name in derived class?
```python
class Parent:
    variable = 12
    
class Derived(Parent):
    variable = 10

Parent.variable # returns 12
```

## 44. Evaulation of boolean expressions
- The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
- The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
```python
x = 'Some Value'
y = 24
z = False
x or y # returns x
z or y # returns y
x and y # returns y
z and x # returns z
```

## 45. Difference between multiprocessing and multithreading
The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. 
- Multithreading is concurrent and is used for IO-bound tasks
- Multiprocessing achieves true parallelism and is used for CPU-bound tasks
Use Multithreading if most of your task involves waiting on API-calls, because why not start up another request in another thread while you wait, rather than have your CPU sit idly by. 

## 46. How to merge two dictionaries together?
```python
first_dict = {'name': 'Tom', 'age': 44}
second_dict = {'occupation': 'actor', 'nationality': 'British'}
# merging
final_dict = {**first_dict, **second_dict}
```
In case any key is repeated in both dictionaries, the second key will hold supremacy. 

## 47. How do you overload a python constructor?

## 48. Explain the below code
```python
def func(sample_list=[]):
    sample_list.append(12)
    # print(id(sample_list))
    return sample_list

print(func()) # [12]
print(func()) # [12,12]
```
 Since list is mutualable type of data structure, the first time func is called, the list is empty, but when the same function is called twice, the list already has an item. We cans sure of the that by printing the id of the sample_list used in the first, on each subsquent call to the function, the id will return the same value. 
 
 ## 49. Example filter with lambda expression.
 ### filter
 filter(function, iterable) # function must return True or False
 ```python
 input_list = ['Delhi', 'Mumbai', 'Noida, 'Gurugram']
 to_match = 'Gurugram'
 
 matched_list = list(filter(lambda item: item == to_match, input_list))
 matched_list # ['Gurugram']
 ```
For every single item in the input_list, the condition is checked in the lambda function which returns either True or False.


## Coding Question
```python
# Transpose a square matrix of n rows and columns
# Write a function that will place even elements of an array at even indexes and odd at odd indexes. 
# Write a function that checks if an array is a subsequence of first array
# Write a function that unzips nested dicts into expanded dicts.
# What is the output of (0,1,2,3,(4,5,6),7,8)[::3]
# Output of a=[[]]*5, a[0].append(1)
# Of a given string, make it an accept python variable name
```
