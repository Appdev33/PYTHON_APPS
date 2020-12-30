import tkinter as tk
import random

# --- function ---

def move():
    #b.place_forget() # it seems I don't have to use it
                      # to hide/remove before I put in new place
    new_x = random.randint(0, 100)
    new_y = random.randint(0, 150)
    b.place(x=new_x, y=new_y)

    b['height'] = random.randint(1, 10)

# --- main ---

root = tk.Tk()

b = tk.Button(root, text='Move it', command=move)
b.place(x=0, y=0)

root.mainloop()