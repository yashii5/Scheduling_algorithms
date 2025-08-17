import tkinter as tk

root = tk.Tk()
root.title("Borderwidth & Relief Demo")

reliefs = ["flat", "ridge", "raised", "sunken", "groove", "solid"]
borderwidths = [0, 1, 2, 5]

row = 0
# Headers
tk.Label(root, text="Relief ↓ / Border →", width=20).grid(row=row, column=0)
for col, bw in enumerate(borderwidths):
    tk.Label(root, text=f"bd={bw}", width=10).grid(row=row, column=col+1)
row += 1

# Show combinations
'''for relief in reliefs:
    tk.Label(root, text=relief, width=20).grid(row=row, column=0)
    for col, bw in enumerate(borderwidths):
        tk.Label(
            root,
            text="Sample",
            relief=relief,
            borderwidth=bw,
            width=10,
            pady=5
        ).grid(row=row, column=col+1, padx=5, pady=5)
    row += 1
'''
root.mainloop()
