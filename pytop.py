import subprocess
import time
from tkinter import *

def update_top():
    top_output = subprocess.run(["top", "-n1"], capture_output=True).stdout.decode()
    top_text.delete(1.0, END)
    top_text.insert(1.0, top_output)
    root.after(3000, update_top)

root = Tk()
top_text = Text(root)
top_text.pack()
update_top()
root.mainloop()
