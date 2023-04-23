import tkinter as tk

# This function will be called when the user clicks the "Write Full Name" button.
# It gets the first and last name from the text boxes, combines them into a full name,
# writes the full name to a file called "names.txt", and prints a message to the console
# confirming that the name was written to the file.
def write_name():
    # Get the first name from the text box
    first_name = first_name_entry.get()
    # Get the last name from the text box
    last_name = last_name_entry.get()
    # Combine the first and last name into a full name
    full_name = f"{first_name} {last_name}"
    # Open the "names.txt" file for appending and write the full name followed by a newline character
    with open("names.txt", "a") as f:
        f.write(full_name + "\n")
    # Print a message to the console confirming that the name was written to the file
    print(f"Full name '{full_name}' written to file.")

# Create the main window
root = tk.Tk()
# Set the window title
root.title("Full Name Writer")

# Create a label and text box for the first name
tk.Label(root, text="First Name:").grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

# Create a label and text box for the last name
tk.Label(root, text="Last Name:").grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

# Create a button labeled "Write Full Name" that calls the write_name() function when clicked
write_button = tk.Button(root, text="Write Full Name", command=write_name)
write_button.grid(row=2, column=0, columnspan=2)

# Start the main event loop to display the window and handle user input
root.mainloop()
