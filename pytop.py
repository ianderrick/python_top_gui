import subprocess  # Import the subprocess module for running shell commands
import time  # Import the time module for the sleep function
from tkinter import *  # Import all functions from the Tkinter library

def update_top():
    # Update the top output displayed in the GUI
    # Run the top command and capture the output
    top_output = subprocess.run(["top", "-n1"], capture_output=True).stdout.decode()
    # Clear the text widget and insert the new output
    top_text.delete(1.0, END)
    top_text.insert(1.0, top_output)
    # Schedule the update_top function to run again in 3 seconds
    root.after(3000, update_top)

# Create the main window
root = Tk()
# Create a text widget to display the top output
top_text = Text(root)
top_text.pack()
# Run the update_top function for the first time
update_top()
# Start the Tkinter event loop
root.mainloop()
