# PYTHON INTERNALS

In this repository we'll learn about Python, not the basic syntaxing and stuff, we'll be deep diving into the internals of how the different data structures and their methods work and much more likewise concepts. 

MINDSET/QUESTIONS while doing Python:
- Is this creating a new object?

- Is Python reusing an existing object?

- Is this mutating or rebinding?

- Why is this fast / slow?


## TOPICS WE'RE COVERING:

### 0. Mental Model (FOUNDATION)

These explain 80 percent of Python behavior:

- Python is an interpreted, dynamic language

- What an object is in Python

- Variables as references, not containers

- Object identity, type, and value

- id() and memory addresses

- Object lifetime

- Singleton objects (None, True, False)

- Name binding vs assignment

- Rebinding vs mutation

- Pass-by-object-reference model

- Operator precedence in python

### 1. Object Model Internals

Core to understanding everything else:

- type, id, dir

- __class__

- Dynamic typing internals

- How attributes are stored

- Instance __dict__

- Class __dict__

- Attribute lookup order

- getattr, setattr, delattr

- __getattribute__ vs __getattr__

- Object mutability model

### 2. Equality and Identity

A major source of bugs.

- == vs is

- Object identity guarantees

- Cached integers

- String interning

- When identity comparison is safe

- Floating point comparison issues

- Hash consistency rules

### 3. Memory Management

Critical for performance and correctness:

- Reference counting

- Garbage collection

- Cyclic garbage collector

- gc module

- Weak references (weakref)

- Object resurrection pitfalls

- Memory leaks in Python

- __del__ dangers

### 4. Built-in Data Structures Internals

(map,filter, reduce)

#### Lists

- How its identifier (of list var.) stores the first element

- Dynamic array implementation

- Overallocation strategy

- Amortized append

- Resize behavior

- Slice mechanics

- Copy vs view behavior

- List comprehension internals

- In-place operations

- Imp list methods for data-science

#### Tuples

- Immutable sequence design

- Memory footprint advantages

- Tuple packing and unpacking

- Hashing behavior

- When tuples outperform lists

- Imp tuple methods for data-science


#### Dictionaries

- Hash table internals

- Open addressing

- Collision resolution

- Resize strategy

- Order preservation (3.7+)

- Key immutability requirement

- Hash randomization

- Dict views vs copies

- Imp dictionary methods for data-science


#### Sets

- Set implementation details

- Deduplication mechanics

- Membership testing performance

- Frozen sets

- Set algebra internals

- Imp set methods for data-science


### 5. String Internals

One of the most optimized parts of Python:

- Unicode string representation

- Immutability consequences

- String interning rules

- Small string optimizations

- Concatenation pitfalls

- join vs +

- Slicing cost

- Encoding vs decoding

- Memory layout of strings

- Imp string methods for data-science


### 6. Function Internals

Functions are objects:

- Function object structure

- Default arguments evaluation

- Mutable default pitfalls

- Closures

- __closure__

- Cell objects

- Function annotations

- Keyword-only arguments

- Positional-only arguments

- *args and **kwargs internals

### 7. Scope and Namespace Resolution

Why some variables behave weirdly:

- LEGB rule

- Local variable optimization

- Global lookup costs

- global and nonlocal

- Fast locals vs globals

- Name shadowing bugs

### 8. Bytecode and Execution Model

Why Python is slower and where:

- Source code to bytecode

- Python virtual machine loop

- Bytecode instructions

- dis module

- Stack-based execution

- Peephole optimizations

- Constant folding

### 9. Truthiness and Boolean Logic

Hidden control flow logic:

- __bool__

- __len__

- Short-circuit evaluation

- Truth value testing rules

- Custom truthiness pitfalls

### 10. Iteration Protocol

Everything iterable follows this:
  
- Iterable vs iterator   (enumerator,zip,etc.).

- __iter__ and __next__

- StopIteration

- Generator internals

- Generator state machine

- yield suspension mechanics


### 11. Comprehensions and Generators

Performance-critical knowledge:

- List comprehension vs loops

- lambda functions

- map, filter, reduce

- Generator expressions

- Scope differences

- Memory usage comparison

- Lazy evaluation internals

### 12. Exception Handling Internals

Expensive but powerful:

- Exception object creation

- Stack unwinding

- Traceback objects

- Cost of try-except

- Control-flow misuse

- Custom exceptions

### 13. Descriptor Protocol (ADVANCED)

This is how Python magic works:

- Descriptor protocol

- __get__, __set__, __delete__

- Bound vs unbound methods

- @property internals

- Class methods

- Static methods

### 14. Class Internals and OOP Mechanics

Deep object-oriented internals:

- Class creation process

- Metaclasses

- type as a metaclass

- MRO (Method Resolution Order)

- C3 linearization

- Multiple inheritance pitfalls

- __slots__

- Dataclasses internals

### 15. Context Managers

Safe resource handling:

- with statement internals

- __enter__, __exit__

- contextlib

- Exception suppression logic

### 16. Concurrency and Parallelism

Critical real-world topic:

- GIL internals

- Thread scheduling

- I/O-bound vs CPU-bound tasks

- Multiprocessing internals

- Asyncio event loop basics

- await and coroutine internals

### 17. Hashing and Security

Subtle but important:

- Hash contract

- Hash randomization

- Custom __hash__

- Equality-hash consistency

- DOS attack prevention

### 18. Copying and Serialization

State handling issues:

- Shallow vs deep copy

- copy module internals

- Pickle protocol

- Serialization pitfalls

- Object identity loss

### 19. Performance Internals

Make Python fast:

- Time complexity realities

- Memory vs speed tradeoffs

- sys.getsizeof

- timeit

- C extensions overview

- NumPy and C API conceptually

### 20. CPython Implementation Details (OPTIONAL BUT POWERFUL)

For serious mastery:

- CPython source tree

- listobject.c

- dictobject.c

- unicodeobject.c

- Reference count macros

- Fast paths

- Why PyPy behaves differently

### 21. Debugging and Introspection Tools

Essential for internals learning:

- inspect

- sys

- gc

- dis

- tracemalloc

- objgraph


### 22. Important Python Libraries

- Flask

- os

- sys

- numpy

- pandas

- beautifulsoup4, lxml

- requests

- subprocess

- re 

- logging

- dis

- timeit

- gc

- json

- joblib