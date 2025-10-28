import tkinter as tk
root = tk.Tk()
root.title("zakhar calculator")
root.geometry("200x200")
root.resizable(False, False)

user_input = ""

input_frame = tk.Frame(root)
button_frame = tk.Frame(root)

input_frame.grid(row=0, column=0)
button_frame.grid(row=1,column=0)

label = tk.Label(input_frame, text=user_input, anchor="w", width=16)
label.grid(row=0, column=0, sticky="w")

def on_click(button):
    global user_input
    user_input+= str(button)
    label.config(text=user_input)

for i in range(10):
    button = tk.Button(button_frame, text= i, command=lambda n=i: on_click(n), width=5)
    button.grid(row=i//3, column=i%3, sticky="w", pady=2)

root.mainloop()