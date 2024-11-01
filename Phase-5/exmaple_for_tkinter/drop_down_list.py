import tkinter as tk
from tkinter import ttk

def submit_form():
    name = entry_name.get()
    selected_option = combobox.get()
    
    print("Name:", name)
    print("Selected Option:", selected_option)

    # You can add further processing logic here
    
    # Close the window after submitting the form
    root.destroy()

root = tk.Tk()
root.title("Form Example")

# Create label and entry field for name
label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Create label and drop-down list for options
label_options = tk.Label(root, text="Select an option:")
label_options.pack()
combobox = ttk.Combobox(root)
combobox['values'] = ('Option 1', 'Option 2', 'Option 3')
combobox.pack()

# Set initial selection
combobox.current(0)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the Tkinter event loop
root.mainloop()