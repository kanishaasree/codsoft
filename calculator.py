import tkinter as tk
from tkinter import ttk

def switch_to_calculator():
    main_frame.tkraise()

def on_click(button_text):
    current_text = entry_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("700x400")
root.configure(bg='#458B74')  

main_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
main_frame.grid(row=0, column=0, sticky="nsew")

start_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
start_frame.grid(row=0, column=0, sticky="nsew")

style = ttk.Style()


style.configure('TFrame', background='#458B74')  


title_label_start = ttk.Label(start_frame, text="Simple Calculator", font=('Arial', 24, 'bold'), foreground='black', background='#458B74')  # Black text, dark goldenrod background
title_label_start.grid(row=0, column=0, pady=(50, 20))


style.configure('Start.TButton', font=('Arial', 14), background='#66CDAA', foreground='#458B74')  # Dark goldenrod1 background, dark goldenrod2 text
start_button = ttk.Button(start_frame, text="Click to Start", style='Start.TButton', command=switch_to_calculator)
start_button.grid(row=1, column=0, pady=(0, 50))


entry_var = tk.StringVar()
entry_var.set("")

entry = ttk.Entry(main_frame, textvariable=entry_var, font=('Arial', 20), justify='right', foreground='black', background='#458B74')  # Black text, dark goldenrod background
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10, sticky="nsew")

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in button_texts:
    style_name = 'Num.TButton' if button_text.isdigit() or button_text == '.' else 'TButton'
    style.configure(style_name, font=('Arial', 14), background='#66CDAA', foreground='#458B74')  # Dark goldenrod1 background, dark goldenrod2 text
    button = ttk.Button(main_frame, text=button_text, style=style_name, command=lambda x=button_text: on_click(x))
    button.grid(row=row_val, column=col_val, ipadx=20, ipady=20, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights for Main Frame
for i in range(1, 6):
    main_frame.grid_rowconfigure(i, weight=1)
    main_frame.grid_columnconfigure(i - 1, weight=1)

# Configure grid weights for Start Frame
start_frame.grid_rowconfigure(0, weight=1)
start_frame.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()
