
import tkinter as tk
import math

# Main Window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("360x540")
root.configure(bg="#151525")
root.resizable(False, False)

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 26),
    bg="#252540",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=25, ipady=18)

# Button functions
def press(value):
    display.insert(tk.END, str(value))

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        result = eval(
            display.get(),
            {"__builtins__": {}},
            {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log10,
                "pi": math.pi,
                "e": math.e
            }
        )
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Button layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "sqrt("],
    ["sin(", "cos(", "tan(", "log("]
]

# Button colors
def button_color(value):
    if value == "=":
        return "#00A878"
    elif value in ["C", "⌫"]:
        return "#D94B65"
    elif value in ["+", "-", "*", "/", "%"]:
        return "#394A80"
    return "#292943"

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#151525")
    frame.pack(expand=True, fill="both", padx=8)

    for item in row:
        btn = tk.Button(
            frame,
            text=item,
            font=("Arial", 15, "bold"),
            bg=button_color(item),
            fg="white",
            activebackground="#5265A0",
            activeforeground="white",
            bd=0,
            command=lambda x=item: (
                clear() if x == "C" else
                backspace() if x == "⌫" else
                calculate() if x == "=" else
                press(x)
            )
        )
        btn.pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )

# Keyboard support
def keyboard(event):
    if event.keysym == "Return":
        calculate()
    elif event.keysym == "Escape":
        clear()

root.bind("<Key>", keyboard)

root.mainloop()
