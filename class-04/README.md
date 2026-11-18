# Class 04 — Python Basics

Checklist from `FOR-STUDENTS-WITHOUT-PROJECTS.md` (the path shown in class:
`C:\ > C-Shaamd-2026-2027 > SCP - Senior Capstone Project`), completed.

## Checklist

| # | Task | Result |
| - | ---- | ------ |
| 1 | Install Python | **Python 3.9.12** — `C:\Users\10256\anaconda3\python.exe` |
| 2 | Write Hello World in Python | `print("Hello World")` |
| 3 | Write Hello World in a Python function | `hello_in_function(name="World")` |
| 4 | Print Hello World five times using a loop | `for i in range(5)` |
| 5 | Make a list of 5 numbers | `[42, 7, 19, 3, 88]` |
| 6 | Print the list of 5 numbers | one number per line |
| 7 | Sort the list of 5 numbers and print it | `[3, 7, 19, 42, 88]` |

## Run it

```bash
python SAM_CLASS_04_PYTHON_BASICS.py
```

## Output

```text
1. Python version: 3.9.12
   interpreter: C:\Users\10256\anaconda3\python.exe

2. Hello World
   Hello World

3. Hello World in a function
   Hello World

4. Hello World five times (loop)
   1. Hello World
   2. Hello World
   3. Hello World
   4. Hello World
   5. Hello World

5. A list of five numbers
   [42, 7, 19, 3, 88]

6. Print the list
   42
   7
   19
   3
   88

7. Sorted list
   original: [42, 7, 19, 3, 88]
   sorted:   [3, 7, 19, 42, 88]
   in place: [3, 7, 19, 42, 88]
```

## Notes

- Sorting is shown twice on purpose: `sorted(numbers)` returns a new list,
  `numbers.sort()` reorders the original in place.
- Only the standard library is used, so it runs on any Python 3.9+ install.
- The first line prints the interpreter version and path — that is the evidence for
  the "install Python" step, in place of a screenshot.
