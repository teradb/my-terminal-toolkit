import tkinter as tk
from tkinter import messagebox

# Global variable to store the mathematical expression string
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        # eval evaluates the mathematical text string directly
        total = str(eval(expression))
        equation.set(total)
        expression = total # Allow further calculations on the result
    except ZeroDivisionError:
        equation.set("Error: Div by 0")
        expression = ""
    except Exception:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Window configurations
window = tk.Tk()
window.title("Visual Grid Calculator")
window.geometry("350x450")
window.configure(bg="#2c3e50")

equation = tk.StringVar()

# Display Screen Entry Box
display_frame = tk.Frame(window, bg="#2c3e50")
display_frame.pack(pady=20)

display = tk.Entry(display_frame, textvariable=equation, font=("Arial", 20, "bold"), 
                   bd=10, insertwidth=4, width=18, borderwidth=0, justify="right", 
                   bg="#34495e", fg="#ffffff")
display.pack()

# Button Layout Grid Frame
button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack()

# Button configuration matrix grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Build and position buttons dynamically inside the grid structure
for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x not in ('=', 'C') else (equalpress() if x == '=' else clear())
    
    # Color accents for operators vs standard numeric digits
    bg_color = "#e67e22" if text in ('/', '*', '-', '+', '=') else ("#c0392b" if text == 'C' else "#ecf0f1")
    fg_color = "#ffffff" if text in ('/', '*', '-', '+', '=', 'C') else "#2c3e50"
    
    btn = tk.Button(button_frame, text=text, font=("Arial", 16, "bold"), width=5, height=2,
                    bg=bg_color, fg=fg_color, command=action, borderwidth=1)
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()

