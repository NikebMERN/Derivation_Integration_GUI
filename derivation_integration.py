import tkinter as tk
from sympy import symbols, sympify, diff, integrate

# Symbol
x = symbols('x')

# Function to compute derivative and integral
def compute():
    input_expr = entry.get()
    try:
        expr = sympify(input_expr)
        derivative = diff(expr, x)
        integral = integrate(expr, x)
        result_label.config(
            text=f"Expression: {expr}\n"
                 f"Derivative: {derivative}\n"
                 f"Integral: {integral} + C"
        )
# C is the constant of integration
    # except (ValueError, TypeError):
    #     result_label.config(text="Invalid expression. Please enter a valid mathematical expression.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Derivative & Integral Calculator")

# Input field
tk.Label(root, text="Enter expression in x:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Button
tk.Button(root, text="Calculate", command=compute).pack(pady=10)

# Output label
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
# This code creates a simple GUI application using Tkinter to compute the derivative and integral of a mathematical expression entered by the user.