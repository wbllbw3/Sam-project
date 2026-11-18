"""Class 04 - Python basics practice.

Covers the checklist from FOR-STUDENTS-WITHOUT-PROJECTS.md:
install Python, Hello World, Hello World in a function, Hello World five times
with a loop, build a list of five numbers, print it, then sort it and print it.

Run with:  python SAM_CLASS_04_PYTHON_BASICS.py
"""

import sys


def hello() -> str:
    """Return the classic greeting."""
    return "Hello World"


def hello_in_function(name: str = "World") -> str:
    """Same greeting, but produced by a function with an argument."""
    return f"Hello {name}"


def five_times() -> list:
    """Build the greeting five times with a loop and return the lines."""
    return [f"{i + 1}. {hello()}" for i in range(5)]


def main() -> None:
    # 1. Python version - proof that the interpreter is installed and reachable
    print(f"1. Python version: {sys.version.split()[0]}")
    print(f"   interpreter: {sys.executable}")

    # 2. Hello World
    print("\n2. Hello World")
    print(f"   {hello()}")

    # 3. Hello World inside a function
    print("\n3. Hello World in a function")
    print(f"   {hello_in_function()}")

    # 4. Hello World five times, using a loop
    print("\n4. Hello World five times (loop)")
    for line in five_times():
        print(f"   {line}")

    # 5. A list of five numbers
    print("\n5. A list of five numbers")
    numbers = [42, 7, 19, 3, 88]
    print(f"   {numbers}")

    # 6. Print the list
    print("\n6. Print the list")
    for n in numbers:
        print(f"   {n}")

    # 7. Sort the list and print it
    print("\n7. Sorted list")
    print(f"   original: {numbers}")
    print(f"   sorted:   {sorted(numbers)}")
    numbers.sort()
    print(f"   in place: {numbers}")


if __name__ == "__main__":
    main()
