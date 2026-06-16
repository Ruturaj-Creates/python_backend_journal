# Intermediate Python Revision Notes

---

# 1. List Comprehensions

## Syntax

```python
new_list = [expression for item in iterable]
```

Example:

```python
squares = [x**2 for x in range(5)]
print(squares)
```

Output:

```python
[0, 1, 4, 9, 16]
```

## With Condition

```python
evens = [x for x in range(10) if x % 2 == 0]
```

## Nested Comprehension

```python
pairs = [(x, y) for x in range(2) for y in range(2)]
```

## Advantages

- Shorter code
- Faster than traditional loops
- More readable

---

# 2. Lambda Functions

## Syntax

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```python
25
```

## Lambda with map()

```python
nums = [1, 2, 3]

result = list(map(lambda x: x * 2, nums))
```

## Lambda with filter()

```python
nums = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, nums))
```

## Lambda with sort()

```python
students = [
    ("A", 23),
    ("B", 20)
]

students.sort(key=lambda x: x[1])
```

---

# 3. *args and **kwargs

## *args

Used to accept multiple positional arguments.

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3))
```

Output:

```python
6
```

Type:

```python
tuple
```

---

## **kwargs

Used to accept multiple keyword arguments.

```python
def profile(**kwargs):
    print(kwargs)

profile(name="John", age=25)
```

Output:

```python
{'name': 'John', 'age': 25}
```

Type:

```python
dict
```

---

## Combined Example

```python
def test(a, *args, **kwargs):
    pass
```

Order:

```python
normal args
*args
**kwargs
```

---

# 4. Exception Handling

Purpose:
Prevent program crashes.

## Basic Syntax

```python
try:
    pass

except:
    pass
```

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## else

Runs only if no exception occurs.

```python
try:
    print(10 / 2)

except:
    print("Error")

else:
    print("Success")
```

---

## finally

Always executes.

```python
try:
    pass

finally:
    print("Cleanup")
```

---

## raise

Manually raise exceptions.

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18+")
```

---

## Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

---

# 5. File Handling

## Open File

```python
file = open("data.txt", "r")
```

---

## Read Entire File

```python
file.read()
```

---

## Read One Line

```python
file.readline()
```

---

## Read All Lines

```python
file.readlines()
```

---

## Write Mode

```python
file = open("data.txt", "w")
```

Creates file if it doesn't exist.

Overwrites existing content.

---

## Append Mode

```python
file = open("data.txt", "a")
```

Adds content to end.

---

## Close File

```python
file.close()
```

---

## Best Practice

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Automatically closes file.

---

# 6. JSON Handling

JSON = JavaScript Object Notation

Used for:
- APIs
- Configuration files
- Data exchange

---

## Import

```python
import json
```

---

## Python Dict → JSON String

```python
data = {"name": "John"}

json_data = json.dumps(data)
```

---

## JSON String → Python Dict

```python
data = json.loads(json_data)
```

---

## Write JSON to File

```python
with open("data.json", "w") as file:
    json.dump(data, file)
```

---

## Read JSON from File

```python
with open("data.json", "r") as file:
    data = json.load(file)
```

---

# Quick Interview Questions

## Difference between append() and extend()?

append():
Adds entire object.

extend():
Adds elements individually.

---

## Difference between read() and readline()?

read():
Entire file.

readline():
One line at a time.

---

## Difference between args and kwargs?

args:
Positional arguments.

kwargs:
Keyword arguments.

---

## Difference between dumps() and dump()?

dumps():
Returns JSON string.

dump():
Writes JSON directly to file.

---

## Difference between loads() and load()?

loads():
Reads JSON string.

load():
Reads JSON file.

---

# Intermediate Python Completed

Topics Covered:

- List Comprehensions
- Lambda Functions
- *args
- **kwargs
- Exception Handling
- File Handling
- JSON Handling