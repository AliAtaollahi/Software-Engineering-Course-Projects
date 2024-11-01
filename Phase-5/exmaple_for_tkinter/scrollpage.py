import tkinter as tk

def mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
root.geometry("400x300")

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Create a canvas
canvas = tk.Canvas(root, bg="white", yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to work with the canvas
scrollbar.config(command=canvas.yview)

# Bind the mouse wheel event to the canvas
canvas.bind_all("<MouseWheel>", mouse_wheel)

# Create a frame inside the canvas for the content
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Add content to the frame (you can add any widgets here)
for i in range(50):
    label = tk.Label(content_frame, text=f"Label {i}", pady=10)
    label.pack()

# Update the canvas scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
