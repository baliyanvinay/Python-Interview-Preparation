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

## 8. How would you load a 4GB data file in Python?

## 9. Explain Generators and use case of it.

## 10. Is there a sequence in defining exceptions in except block for exception handling?

## Coding Question
```python
# Transpose a square matrix of n rows and columns
# Write a function that will place even elements of an array at even indexes and odd at odd indexes. 
# Write a function that checks if an array is a subsequence of first array
```
