# Derivative and Integral Calculator (Python GUI)

## 📌 Concept Overview
This project is a symbolic math calculator that allows a user to enter a mathematical expression and see its derivative and indefinite integral. It's implemented in Python using the sympy library for math and tkinter for GUI.

## 🔍 What Are Derivation and Integration?
✅ Derivative (Differentiation):
Measures how fast a function changes at any point.

Think of it as the slope of a curve.

Example:
If f(x) = x², then the derivative f'(x) = 2x.
This means the slope of the curve at any point x is 2x.

✅ Integral (Integration):
Represents the area under the curve of a function.

Think of it as accumulating values over time or space.

Example:
If f(x) = x², then the integral ∫f(x)dx = (1/3)x³ + C
The + C is the constant of integration, since integration is not unique.

## 🧠 Technical Terms
| Term                 | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| `sympy`              | Python library for symbolic math (like algebra, calculus).               |
| `diff(expr, x)`      | Derives `expr` with respect to variable `x`.                             |
| `integrate(expr, x)` | Integrates `expr` with respect to variable `x`.                          |
| `sympify()`          | Converts a string like `'x**2 + 3*x'` into a math object.                |
| `tkinter`            | Python's built-in library for building graphical user interfaces (GUIs). |
| `Entry`              | A textbox widget in tkinter for user input.                              |
| `Label`              | A widget that displays text in the GUI.                                  |

## 🧾 How the Code Works (Simplified)
1. Import libraries: sympy for math, tkinter for GUI.

2. Create a GUI window where the user can:

3. Enter an expression (e.g. x**2 + 3*x)

4. Click a "Calculate" button

5. On button click, it:

6. Reads the expression

7. Converts it to a symbolic format (sympify)

8. Calculates the derivative and integral

9. Displays results on the screen

                                      # Prepared by: Nikodimos Elias G/Egziabher
                                      # Junior Software Developer
