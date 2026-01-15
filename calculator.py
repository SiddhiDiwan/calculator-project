



















import tkinter as tk


def button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)


def clear():
    entry_var.set("")


def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")


root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry_var = tk.StringVar()


entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

frame = tk.Frame(root)
frame.pack()


for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(row_frame, text=btn_text, width=5, height=2,
                            font=("Arial", 18), command=calculate)
        else:
            btn = tk.Button(row_frame, text=btn_text, width=5, height=2,
                            font=("Arial", 18), command=lambda val=btn_text: button_click(val))
        btn.pack(side="left", padx=5, pady=5)


clear_btn = tk.Button(root, text="CLEAR", font=("Arial", 16), bg="red", fg="white",
                      command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)


root.mainloop()