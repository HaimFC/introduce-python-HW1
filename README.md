
# Homework Assignment 1 - Solutions

### General Information
- **Responsible Teaching Assistant**: Ariel Cohen
- For quick answers regarding this assignment, please ask in Piazza under the label HW1.
- Office hours: Thursday, 17:00–18:00 (Email coordination required).

---

## Structure
The program receives the question number as input. Based on the question number, additional inputs will be provided. The program executes and produces outputs as follows:

---

### Question 1 - Vowels
The program counts the number of letters in a given string that are not lowercase vowels (a, e, i, o, u, y). The letter `y` is considered a vowel.

#### Example
Input:
```
programming is fun
```
Output:
```
13
```

---

### Question 2 - Taylor Approximation
The program calculates the Taylor approximation (of order `n`) for the expression `ln(1 + x)` around the point `x`. 

#### Validity Constraints
- `x` must be a float satisfying `-0.7 ≤ x ≤ 0.7`.
- `n` must be a positive integer.

#### Example
Input:
```
x = 0.5, n = 3
```
Output:
```
Taylor approximation result
```

---

### Question 3 - Playing with Strings
The program manipulates a string such that:
1. Words at even indices are converted to uppercase.
2. Words at odd indices are converted to lowercase.
3. Uppercase words are sorted lexicographically (ascending).
4. Lowercase words are sorted lexicographically (descending).

#### Example
Input:
```
banana apple pear
```
Output:
```
APPLE banana pear
```

---

### Question 4 - Lychrel Numbers
The program checks if a number is a potential Lychrel number:
1. A Lychrel candidate exceeds 500 iterations without forming a palindrome.
2. Otherwise, it prints the number of iterations required to form a palindrome.

#### Example
Input:
```
196
```
Output:
```
True
```
---
