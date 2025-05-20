# SANGU-VENKATA-PRASHANTH-REDDY
## 💻 Language Used
Python 3

---

## 📁 Files Included

| File Name      | Description                                   |
|----------------|-----------------------------------------------|
| python-1.py    | Calculator using class for +, -, *, /         |
| python-2.py    | Print first `a` odd numbers                   |
| python-3.py    | Print `a` or `a-1` odd numbers based on input |
| python-4.py    | Count how many numbers are divisible by 1–9   |

---

## 🔍 Problem-wise Details and Approaches

### ✅ `python-1.py` - **Basic Calculator**

**Objective**: Build a calculator class that supports addition, subtraction, multiplication, and division.

**Approach**:
- Created a `Calculator` class with an `__init__` method to store two numbers: `a` and `b`.
- Defined 4 methods: `add()`, `subtract()`, `multiply()`, and `divide()`.
- Used user input to get `a`, `b`, and the operation symbol (`+`, `-`, `*`, `/`).
- Used if-else logic to call the appropriate method.

**Highlights**:
- Exception handling for division by zero.
- Demonstrates class and object-oriented design.

---

### ✅ `python-2.py` - **Print First 'a' Odd Numbers**

**Objective**: Print the first `a` odd numbers starting from 1.

**Approach**:
- Defined a function `oddseries(a)` that uses a loop `for i in range(a)` to generate the first `a` odd numbers.
- Formula used: `2 * i + 1`
- Stored the results in a list and printed them as a comma-separated string.

**Highlights**:
- Uses list and string manipulation.
- Simple arithmetic sequence logic.

---

### ✅ `python-3.py` - **Odd Series Based on Even/Odd Input**

**Objective**: 
- If input `a` is odd → print first `a` odd numbers.
- If input `a` is even → print first `a-1` odd numbers.

**Approach**:
- Used `if a % 2 == 0` to check if the number is even.
- Created a `series()` function that generates odd numbers using the same formula: `2 * i + 1`.
- Reused logic from Problem-2 with a slight twist in the count.

**Highlights**:
- Uses conditional logic to control the series length.
- Shows modular code reuse.

---

### ✅ `python-4.py` - **Count Divisibles from List**

**Objective**: Count how many numbers in a list are divisible by each digit from 1 to 9.

**Approach**:
- Defined a function `count(l)` that loops from 1 to 9.
- For each `i` in 1–9, it checks every element in the list to see if `element % i == 0`.
- Maintains a count for each divisor and stores it in a dictionary.
- Finally prints the dictionary.

**Highlights**:
- Uses nested loops and modulus operator.
- Shows use of dictionaries and efficient counting logic.

---

## ▶️ How to Run

Each program is standalone. Use any Python 3 interpreter or terminal.

```bash
python python-1.py
python python-2.py
python python-3.py
python python-4.py
