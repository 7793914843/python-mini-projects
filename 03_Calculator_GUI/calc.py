
import tkinter as tk


# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")


# Display
entry = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="ew"
)


# Add number/operator
def click(value):
    entry.insert(tk.END, value)


# Clear display
def clear():
    entry.delete(0, tk.END)


# Calculate result
def calculate():

    try:
        expression = entry.get()

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("=", 4, 3)
]


# Create buttons
for text, row, column in buttons:

    if text == "=":

        button = tk.Button(
            window,
            text=text,
            font=("Arial", 18),
            command=calculate
        )

    else:

        button = tk.Button(
            window,
            text=text,
            font=("Arial", 18),
            command=lambda value=text: click(value)
        )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        ipadx=10,
        ipady=10
    )


# Clear button
clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 18),
    command=clear
)

clear_button.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10,
    ipadx=40,
    ipady=5
)


