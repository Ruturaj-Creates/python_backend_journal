# Python Corporate Revision Notes

## 1. Data Types

### Primitive Types

```python
name = "John"      # str
age = 25           # int
salary = 45000.50  # float
is_active = True   # bool
```

### Collections

```python
lst = [1, 2, 3]            # List
tup = (1, 2, 3)            # Tuple
st = {1, 2, 3}             # Set
dct = {"name": "John"}     # Dictionary
```

---

## 2. Control Flow

### Conditionals

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Loops

```python
for item in items:
    print(item)

while condition:
    pass
```

---

## 3. Functions

```python
def add(a: int, b: int) -> int:
    return a + b
```

### *args and **kwargs

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

## 4. List Comprehensions

```python
squares = [x*x for x in range(5)]
```

### Conditional

```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 5. Lambda Functions

```python
square = lambda x: x * x
```

Used in:

```python
sorted(users, key=lambda x: x["age"])
```

---

## 6. Exception Handling

```python
try:
    value = int(input())
except ValueError:
    print("Invalid Input")
finally:
    print("Completed")
```

### Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

---

## 7. File Handling

```python
with open("data.txt", "r") as file:
    content = file.read()
```

Modes:

* r
* w
* a
* rb
* wb

---

## 8. Modules & Packages

```python
import math
from datetime import datetime
```

Create reusable code using modules.

---

## 9. OOP

### Class

```python
class Employee:
    def __init__(self, name):
        self.name = name
```

### Inheritance

```python
class Manager(Employee):
    pass
```

### Encapsulation

```python
self.__salary
```

### Polymorphism

```python
obj.method()
```

### Important Dunder Methods

```python
__init__
__str__
__repr__
__len__
```

---

## 10. Iterators & Generators

### Generator

```python
def numbers():
    yield 1
    yield 2
```

### Generator Expression

```python
gen = (x*x for x in range(10))
```

Benefits:

* Lazy loading
* Memory efficient

---

## 11. Decorators

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Running")
        return func(*args, **kwargs)
    return wrapper
```

Usage:

```python
@logger
def greet():
    pass
```

Real Use Cases:

* Logging
* Authentication
* Authorization
* Timing

---

## 12. Context Managers

```python
with open("file.txt") as f:
    data = f.read()
```

Custom:

```python
__enter__()
__exit__()
```

Purpose:

* Resource management
* Database connections
* File handling

---

## 13. Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

Complex Types:

```python
list[str]
dict[str, int]
Optional[str]
Union[int, str]
```

---

## 14. Async Programming

```python
import asyncio

async def task():
    await asyncio.sleep(1)
```

Important:

* async
* await
* asyncio.gather()
* create_task()

Use Cases:

* APIs
* Microservices
* Concurrent I/O

---

## 15. Common Built-in Functions

```python
map()
filter()
zip()
enumerate()
sorted()
any()
all()
sum()
min()
max()
```

---

## 16. Collections Module

```python
from collections import Counter, defaultdict, deque
```

### Counter

```python
Counter("banana")
```

### defaultdict

```python
defaultdict(list)
```

---

## 17. Dataclasses

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Benefits:

* Less boilerplate
* Cleaner models

---

## 18. Virtual Environments

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install:

```bash
pip install requests
```

Requirements:

```bash
pip freeze > requirements.txt
```

---

## 19. JSON Handling

```python
import json

json.dumps(data)
json.loads(data)
```

Used in:

* REST APIs
* Configuration Files

---

## 20. Corporate Must-Know Modules

```python
datetime
pathlib
os
sys
json
logging
collections
typing
dataclasses
asyncio
```

---

## 21. Logging

```python
import logging

logging.info("Application started")
logging.error("Something failed")
```

Avoid excessive print statements in production code.

---

## 22. Clean Code Rules

* Use meaningful variable names
* Write small functions
* Add type hints
* Handle exceptions properly
* Avoid global variables
* Follow PEP8
* Write docstrings

---

## 23. Interview Revision Checklist

* OOP
* Exception Handling
* List Comprehensions
* Decorators
* Generators
* Context Managers
* Type Hints
* Async/Await
* Collections Module
* Dataclasses
* JSON
* Logging
* Virtual Environments
* Iterators
* Time Complexity Basics
