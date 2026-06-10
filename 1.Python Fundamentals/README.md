# 🐍 Python — Zero to Advanced

> A complete, self-taught Python journey from absolute beginner to advanced level.  
> Every concept learned hands-on, every project built from scratch.

<br>

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-f0a500?style=flat)
![Chapters](https://img.shields.io/badge/Chapters%20Completed-12%20%2F%2016-brightgreen?style=flat)
![Projects](https://img.shields.io/badge/Projects-4-blueviolet?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat)

---

## 👋 About This Repository

This repo documents my complete Python learning journey — starting from zero programming knowledge and working through every core concept up to advanced Python.

Each chapter contains:
- 📝 Concept explanations with real-life analogies
- 💻 Clean, commented code examples
- 🧪 Practice exercises with solutions
- 🏗️ Mini projects applying the concepts

---

## 🗂️ Table of Contents

| # | Chapter | Topics Covered | Status |
|---|---------|----------------|--------|
| 0 | [What is Programming?](#chapter-0) | Python intro, installation, first program | ✅ Done |
| 1 | [Modules, Comments & pip](#chapter-1) | import, pip, math, random, os, sys | ✅ Done |
| 2 | [Variables & Datatypes](#chapter-2) | int, float, str, bool, None, operators, input() | ✅ Done |
| 3 | [Strings](#chapter-3) | Indexing, slicing, methods, f-strings, regex intro | ✅ Done |
| 4 | [Lists & Tuples](#chapter-4) | Indexing, methods, nested lists, unpacking | ✅ Done |
| 5 | [Dictionaries & Sets](#chapter-5) | CRUD operations, methods, set operations | ✅ Done |
| 6 | [Conditional Expressions](#chapter-6) | if/elif/else, logical operators, ternary | ✅ Done |
| 7 | [Loops in Python](#chapter-7) | for, while, break, continue, list comprehension | ✅ Done |
| 8 | [Functions & Recursion](#chapter-8) | def, return, *args, **kwargs, lambda, recursion | ✅ Done |
| 🎮 | [Project 1 — Snake, Water, Gun](#project-1) | Game logic, random, functions | ✅ Done |
| 9 | [File I/O](#chapter-9) | read/write, CSV, JSON, os module, error handling | ✅ Done |
| 10 | [Object Oriented Programming](#chapter-10) | Classes, objects, __init__, methods, encapsulation | ✅ Done |
| 11 | [Inheritance & More OOP](#chapter-11) | Inheritance, super(), polymorphism, abstraction | ✅ Done |
| 🎮 | [Project 2 — The Perfect Guess](#project-2) | OOP game, difficulty levels, scoring system | ✅ Done |
| 12 | [Advanced Python 1](#chapter-12) | Exceptions, generators, decorators, map/filter/zip, RegEx | ✅ Done |
| 13 | [Advanced Python 2](#chapter-13) | Multithreading, context managers, metaclasses | 🔄 In Progress |
| 🤖 | [Mega Project 1 — Jarvis AI](#mega-project-1) | AI assistant, speech recognition, APIs | 🔜 Coming Soon |
| 🤖 | [Mega Project 2 — Auto Reply Chatbot](#mega-project-2) | NLP, automation, chatbot logic | 🔜 Coming Soon |

---

## 📚 Chapter Breakdown

### Chapter 0
**What is Programming?**
- What programming is and why Python
- Installing Python and VS Code
- Writing and running the first program
- Understanding errors and how to read them
- Computational thinking basics

---

### Chapter 1
**Modules, Comments & pip**
- Single-line and multi-line comments
- Importing built-in modules (`math`, `random`, `os`, `sys`, `datetime`)
- `import module`, `from module import x`, `import module as alias`
- Installing third-party packages with `pip`
- `pip install`, `pip list`, `pip freeze > requirements.txt`

---

### Chapter 2
**Variables & Datatypes**
- Variables as named containers
- Core datatypes: `int`, `float`, `str`, `bool`, `None`
- Type conversion: `int()`, `float()`, `str()`, `bool()`
- `input()` and why it always returns a string
- Arithmetic operators: `+ - * / // % **`
- Shortcut operators: `+= -= *= /=`
- Naming conventions: `snake_case`

---

### Chapter 3
**Strings**
- String indexing (forward and negative)
- Slicing with `[start:stop:step]`
- Reversing a string with `[::-1]`
- Built-in methods: `upper()`, `lower()`, `strip()`, `split()`, `replace()`, `find()`, `count()`
- f-strings for clean string formatting
- Escape sequences: `\n`, `\t`, `\\`, `\"`
- String immutability

---

### Chapter 4
**Lists & Tuples**
- Creating, indexing, and slicing lists
- Modifying: `append()`, `insert()`, `extend()`, `remove()`, `pop()`
- Sorting and reversing: `sort()`, `reverse()`, `sorted()`
- `min()`, `max()`, `sum()`, `len()`
- Tuples vs lists: when to use each
- Tuple unpacking and variable swapping
- Nested lists (2D arrays)

---

### Chapter 5
**Dictionaries & Sets**
- Creating and accessing dictionaries
- Safe access with `.get()`
- CRUD: add, update, delete keys
- Methods: `keys()`, `values()`, `items()`, `update()`, `pop()`
- Nested dictionaries
- Sets: unique collections, no order
- Set operations: union `|`, intersection `&`, difference `-`
- Removing list duplicates using sets

---

### Chapter 6
**Conditional Expressions**
- `if`, `elif`, `else` chains
- Comparison operators: `== != < > <= >=`
- Logical operators: `and`, `or`, `not`
- Nested conditionals
- Ternary operator: `x if condition else y`
- Python's mandatory indentation

---

### Chapter 7
**Loops in Python**
- `for` loops with `range(start, stop, step)`
- Looping over lists, strings, dicts
- `enumerate()` for index + value
- `while` loops with counters
- `break`, `continue`, `pass`
- Nested loops and patterns
- List comprehensions: `[expr for x in iterable if condition]`

---

### Chapter 8
**Functions & Recursion**
- Defining and calling functions with `def`
- Parameters, arguments, and `return`
- Default parameters
- `*args` (tuple of extra positional args)
- `**kwargs` (dict of extra keyword args)
- Lambda functions: `lambda x: x**2`
- Recursion with mandatory base cases
- DRY principle in practice

---

### Project 1
**Snake, Water, Gun Game** 🎮
- Complete CLI game (Indian Rock-Paper-Scissors)
- Random computer choice using `random.choice()`
- Win/loss/draw logic with a dictionary
- Score tracking across multiple rounds
- Input validation and clean game loop

---

### Chapter 9
**File I/O**
- Opening files with `with open()` (context manager)
- Modes: `"r"`, `"w"`, `"a"`, `"r+"`, `"rb"`, `"wb"`
- Reading: `read()`, `readline()`, `readlines()`, direct iteration
- Writing: `write()`, `writelines()`
- CSV: `csv.reader`, `csv.writer`, `csv.DictReader`
- JSON: `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`
- `os` module: `getcwd()`, `makedirs()`, `rename()`, `remove()`, `path.exists()`
- Safe file handling with `try/except`
- Mini project: Personal Diary App with JSON persistence

---

### Chapter 10
**Object Oriented Programming**
- Classes as blueprints, objects as instances
- `__init__` constructor and `self`
- Instance attributes vs class attributes
- Instance methods and the role of `self`
- `__str__` for human-readable object representation
- Encapsulation with private attributes (`__variable`)
- Controlled access via getter methods
- Mini project: Library Management System

---

### Chapter 11
**Inheritance & More OOP**
- Single inheritance: `class Child(Parent)`
- `super()` to call parent constructor and methods
- Method overriding
- Polymorphism: same method name, different behavior per class
- Abstract classes with `abc.ABC` and `@abstractmethod`
- `isinstance()` and `issubclass()` checks
- Mini project: Perfect Guess game (OOP version with difficulty levels)

---

### Project 2
**The Perfect Guess** 🎮
- Full OOP design with a `GuessingGame` class
- Three difficulty levels (Easy / Medium / Hard)
- Dynamic hint system: direction + temperature feedback
- Score calculation based on attempts used
- Win rate tracking and player ranking system

---

### Chapter 12
**Advanced Python 1**
- `try / except / else / finally`
- Common exceptions: `ValueError`, `TypeError`, `IndexError`, `KeyError`, etc.
- `raise` to trigger exceptions manually
- Custom exception classes
- Iterators: `__iter__` and `__next__`
- Generators with `yield` — memory-efficient data pipelines
- Generator expressions `(x for x in ...)`
- Decorators: wrapping functions with `@decorator`
- `functools.wraps` to preserve metadata
- Practical decorators: `@timer`, `@logger`, `@retry`, `@validate`
- Stacking multiple decorators
- `map()`, `filter()`, `zip()`, `reduce()`
- List, dict, and set comprehensions
- Nested comprehensions and matrix transposition
- `any()`, `all()`, `sorted()` with custom keys
- Regular expressions with the `re` module
- `datetime` and `timedelta` for date arithmetic
- Virtual environments with `venv`
- Mini project: Smart Student Grade Analyzer

---

## 🏗️ Projects

### Project 1 — Snake, Water, Gun Game
A complete terminal game implementing the classic hand game with score tracking and input validation.

**Concepts used:** functions, random, dictionaries, loops, conditionals

```
📁 projects/snake_water_gun/
    └── game.py
```

---

### Project 2 — The Perfect Guess
A number guessing game with three difficulty levels, a smart hint engine, and a scoring + ranking system — built entirely with OOP.

**Concepts used:** classes, methods, encapsulation, conditionals, loops, f-strings

```
📁 projects/perfect_guess/
    └── game.py
```

---

### Project 3 — Personal Diary App *(Chapter 9)*
A persistent diary application that saves, searches, and manages entries using JSON file storage.

**Concepts used:** File I/O, JSON, os module, datetime, exception handling

```
📁 projects/diary_app/
    └── diary.py
```

---

### Project 4 — Student Grade Analyzer *(Chapter 12)*
Analyzes student grades with rankings, pass/fail stats, visual score bars, and JSON persistence.

**Concepts used:** OOP, comprehensions, map/filter, reduce, RegEx, decorators, file I/O

```
📁 projects/grade_analyzer/
    └── analyzer.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| VS Code | Editor |
| Git & GitHub | Version control |
| `venv` | Virtual environment |
| Standard Library | `os`, `json`, `csv`, `re`, `datetime`, `math`, `random`, `abc`, `functools` |

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/iamshahid22/Python-Full-Stack-Zero---Advanced-.git

# 2. Navigate into it
cd Python-Full-Stack-Zero---Advanced-

# 3. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 4. Install dependencies (if any)
pip install -r requirements.txt

# 5. Run any chapter or project
python chapters/chapter_02_variables.py
python projects/snake_water_gun/game.py
```

---

## 📁 Folder Structure

```
Python-Full-Stack-Zero---Advanced-/
│
├── chapters/
│   ├── chapter_00_intro.py
│   ├── chapter_01_modules.py
│   ├── chapter_02_variables.py
│   ├── chapter_03_strings.py
│   ├── chapter_04_lists_tuples.py
│   ├── chapter_05_dict_sets.py
│   ├── chapter_06_conditionals.py
│   ├── chapter_07_loops.py
│   ├── chapter_08_functions.py
│   ├── chapter_09_file_io.py
│   ├── chapter_10_oop.py
│   ├── chapter_11_inheritance.py
│   └── chapter_12_advanced.py
│
├── projects/
│   ├── snake_water_gun/
│   ├── perfect_guess/
│   ├── diary_app/
│   └── grade_analyzer/
│
├── exercises/
│   └── (practice problems per chapter)
│
├── requirements.txt
└── README.md
```

---

## 📈 Progress

```
Chapter 0   ████████████████████  100%  ✅
Chapter 1   ████████████████████  100%  ✅
Chapter 2   ████████████████████  100%  ✅
Chapter 3   ████████████████████  100%  ✅
Chapter 4   ████████████████████  100%  ✅
Chapter 5   ████████████████████  100%  ✅
Chapter 6   ████████████████████  100%  ✅
Chapter 7   ████████████████████  100%  ✅
Chapter 8   ████████████████████  100%  ✅
Chapter 9   ████████████████████  100%  ✅
Chapter 10  ████████████████████  100%  ✅
Chapter 11  ████████████████████  100%  ✅
Chapter 12  ████████████████████  100%  ✅
Chapter 13  ████░░░░░░░░░░░░░░░░   20%  🔄
Jarvis AI   ░░░░░░░░░░░░░░░░░░░░    0%  🔜
AI Chatbot  ░░░░░░░░░░░░░░░░░░░░    0%  🔜
```

---

## 🎯 What's Next

- [ ] Chapter 13 — Advanced Python 2 (multithreading, context managers)
- [ ] Mega Project 1 — Jarvis AI Assistant
- [ ] Mega Project 2 — Auto Reply AI Chatbot
- [ ] Django web development track
- [ ] DSA in Python (LeetCode practice)

---

## 🙋‍♂️ About Me

**Shahid** — Final year B.Tech CSE student & Python Full Stack Developer in training.

Building real skills, one chapter at a time. 🐍

[![GitHub](https://img.shields.io/badge/GitHub-iamshahid22-181717?style=flat&logo=github)](https://github.com/iamshahid22)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with consistency, curiosity, and a lot of <code>print()</code> statements.</sub>
</div>