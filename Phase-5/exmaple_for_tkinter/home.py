import tkinter as tk

def show_page(page):
    # Hide all pages
    for p in pages:
        p.pack_forget()

    # Show the selected page
    page.pack()

# Create the main window
root = tk.Tk()
root.title("My Site")

# Create the pages as frames
page1 = tk.Frame(root)
page2 = tk.Frame(root)
pages = [page1, page2]

# Add widgets to page 1
label1 = tk.Label(page1, text="Welcome to Page 1!")
label1.pack()

button1 = tk.Button(page1, text="Go to Page 2", command=lambda: show_page(page2))
button1.pack()

# Add widgets to page 2
label2 = tk.Label(page2, text="Welcome to Page 2!")
label2.pack()

button2 = tk.Button(page2, text="Go to Page 1", command=lambda: show_page(page1))
button2.pack()

# Initially show page 1
show_page(page1)

# Start the tkinter event loop
root.mainloop()
