# Advanced Python Revision Notes

---

# 1. OOP (Object-Oriented Programming)

## Why OOP?

OOP helps organize code into reusable and maintainable structures.

Instead of storing data and functions separately:

```text
User Data
User Functions

Product Data
Product Functions
```

We combine them into objects.

```text
User
├── data
└── behavior
```

---

## Core Concepts

### Class

Blueprint for creating objects.

Example:

```text
Car
├── color
├── brand
└── start()
```

A class doesn't occupy memory for actual data until an object is created.

---

### Object

Instance of a class.

```python
car = Car()
```

Each object maintains its own state.

---

### Constructor (**init**)

Runs automatically when an object is created.

Purpose:

* Initialize attributes
* Set default values

Think of it as object setup logic.

---

### Inheritance

Allows one class to reuse another class.

```text
Animal
├── eat()
└── sleep()

Dog
├── eat()
├── sleep()
└── bark()
```

Benefits:

* Code reuse
* Better organization
* Easier maintenance

---

### Polymorphism

Same interface, different implementation.

Example:

```text
Dog.sound()   -> Bark
Cat.sound()   -> Meow
```

Code can work with different objects without knowing their exact type.

Very common in frameworks.

---

### Encapsulation

Hide internal implementation.

```text
Public Methods
      ↓
Private Data
```

Benefits:

* Data protection
* Controlled access
* Cleaner APIs

---

### Abstraction

Expose only necessary details.

Example:

You drive a car without knowing engine internals.

Goal:

```text
Use functionality
without understanding implementation
```

---

### When Used In Corporate Projects?

* Backend APIs
* Service classes
* Database models
* Business logic layers
* Design patterns

---

# 2. Decorators

## What Problem Do Decorators Solve?

Suppose many functions need:

* Logging
* Authentication
* Authorization
* Timing
* Retry logic

Without decorators:

```text
Function A
Function B
Function C

Repeat logging code everywhere
```

Decorator wraps functionality around a function.

---

## Mental Model

```text
Before Function
Run Function
After Function
```

Decorator acts like middleware.

---

## How It Works

Functions are first-class objects in Python.

Meaning:

* Store in variables
* Pass as arguments
* Return from functions

Decorator simply receives a function and returns a modified version.

---

## Real Corporate Uses

### Logging

```text
Request Started
Request Ended
```

### Authentication

```text
Check user login
Run API
```

### Timing

```text
Measure execution time
```

### Retry Logic

```text
API failed
Retry automatically
```

---

# 3. Generators

## Problem

Creating huge lists consumes memory.

```python
nums = [1...10000000]
```

Entire list loads into memory.

---

## Generator Solution

Generate values only when needed.

```text
Need value?
Generate it.
```

Not stored permanently.

---

## Yield Keyword

`yield` pauses execution and remembers state.

Next call continues from previous position.

Think:

```text
return -> function ends

yield -> function pauses
```

---

## Benefits

### Memory Efficient

Only one value exists at a time.

### Faster Startup

No need to create full collection first.

### Streaming Data

Useful for:

* Log files
* CSV processing
* Large datasets
* API pagination

---

## Generator Expression

Lazy version of list comprehension.

```python
(x*x for x in range(1000))
```

---

## Corporate Usage

* Reading files
* ETL pipelines
* Data processing
* Streaming systems

---

# 4. Context Managers

## Problem

Resources must be cleaned up.

Example:

```text
Open file
Read file
Close file
```

What if exception occurs?

File may remain open.

---

## Context Manager Solution

Automatically handles setup and cleanup.

```text
Enter Block
Work
Exit Block
```

Guaranteed cleanup.

---

## with Statement

```python
with open(...) as f:
```

Python automatically closes file.

---

## Internal Methods

### **enter**()

Runs before block.

Used for:

* Open connection
* Acquire resource

---

### **exit**()

Runs after block.

Used for:

* Close connection
* Release resource

Runs even if exception occurs.

---

## Corporate Usage

### Database Connections

```text
Connect
Query
Disconnect
```

### File Handling

```text
Open
Read
Close
```

### Locks

```text
Acquire Lock
Execute
Release Lock
```

---

# 5. Type Hints

## Purpose

Python is dynamically typed.

```python
x = 10
x = "hello"
```

Flexible but error-prone.

---

## Type Hints Add Clarity

```python
def add(a: int, b: int) -> int
```

Benefits:

### Better Readability

Developer immediately understands expected types.

---

### IDE Support

Auto-completion improves.

---

### Static Analysis

Tools detect mistakes before execution.

Examples:

* mypy
* pyright

---

## Important Types

### Basic

```text
int
str
float
bool
```

---

### Collections

```text
list[str]
dict[str, int]
set[int]
tuple[str, int]
```

---

### Optional

```text
Value may be None
```

---

### Union

```text
Multiple possible types
```

---

## Corporate Usage

Large codebases.

Type hints become documentation.

Many companies require them.

---

# 6. Async/Await

## Problem

Traditional code waits.

Example:

```text
Call API
Wait

Call Database
Wait

Call Service
Wait
```

CPU stays idle.

---

## Async Solution

While waiting, do other work.

```text
Task A waiting

Run Task B
Run Task C
```

Better utilization.

---

## Coroutine

Function declared using:

```python
async def
```

Coroutine can pause execution.

---

## await

Pause current task until result arrives.

Does NOT block entire program.

---

## Event Loop

Heart of async programming.

Responsible for:

```text
Schedule Tasks
Pause Tasks
Resume Tasks
```

---

## asyncio.gather()

Run multiple tasks concurrently.

Example:

```text
API 1
API 2
API 3
```

All start together.

---

## When Async Helps

Good For:

* APIs
* Databases
* File I/O
* Network calls

---

## When Async Doesn't Help

CPU-heavy tasks:

```text
Image Processing
Machine Learning
Encryption
```

Use multiprocessing instead.

---

# Quick Revision Before Solving Questions

## OOP

Ask:

```text
What problem does OOP solve?
Why inheritance?
Why polymorphism?
```

---

## Decorators

Ask:

```text
Why wrap functions?
What reusable behavior can be extracted?
```

---

## Generators

Ask:

```text
Why use yield instead of return?
How does it save memory?
```

---

## Context Managers

Ask:

```text
What resource is being managed?
What happens during cleanup?
```

---

## Type Hints

Ask:

```text
What type enters?
What type leaves?
Why does readability improve?
```

---

## Async

Ask:

```text
Is the task waiting for I/O?
Can multiple waits happen together?
```

---

# Interview One-Liners

OOP:
"Organizes code into reusable objects that combine data and behavior."

Decorators:
"Allow behavior to be added to functions without modifying their source code."

Generators:
"Produce values lazily, saving memory."

Context Managers:
"Manage resource acquisition and cleanup automatically."

Type Hints:
"Improve readability, tooling support, and static analysis."

Async/Await:
"Enable concurrent I/O operations without blocking the event loop."
