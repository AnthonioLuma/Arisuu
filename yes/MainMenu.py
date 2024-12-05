from tkinter import *

def open_cashier_window():
    window.destroy()  # Close the current window
    cashier_window = Tk()  # Create a new main window
    cashier_window.title("Cashier")
    cashier_window.geometry("800x600")  # Set size for the cashier window
    Label(cashier_window, text="Welcome to the Cashier!", font=("Times New Roman", 16)).pack(pady=20)

def open_inventory_window():
    window.destroy()  # Close the current window
    inventory_window = Tk()  # Create a new main window
    inventory_window.title("Inventory")
    inventory_window.geometry("800x600")  # Set size for the inventory window
    Label(inventory_window, text="Welcome to the Inventory!", font=("Times New Roman", 16)).pack(pady=20)

def open_supply_window():
    window.destroy()  # Close the current window
    supply_window = Tk()  # Create a new main window
    supply_window.title("Supply")
    supply_window.geometry("800x600")  # Set size for the supply window
    Label(supply_window, text="Welcome to the Supply!", font=("Times New Roman", 16)).pack(pady=20)

def exit_application():
    window.destroy()

def create_button(text, command=None):
    button = Button(window,
                    text=text,
                    font=("Times New Roman", 20),
                    fg="#1893f8",  # Set text color to #1893f8
                    bg="white",  # White background
                    state=ACTIVE,  # Keep state as ACTIVE
                    compound='bottom',
                    width=30,
                    highlightthickness=0,  # Remove highlight border
                    highlightcolor="white",  # Set highlight color to match the background
                    activebackground="white",  # Match active background to the button's background
                    activeforeground="#1893f8",  # Keep the text color the same for active state
                    command=command  # Set the command for the button
                    )
    button.pack(pady=20, padx=20)  # Use pack layout with padding

window = Tk()
window.title("Arisu Inventory System")
window.configure(bg="#97bcc7")  # Light blue background
window.geometry("800x600")  # Set window size to 800x600 pixels

# Pass the function reference without parentheses
create_button("Cashier", open_cashier_window)
create_button("Inventory", open_inventory_window)
create_button("Supply", open_supply_window)
create_button("Exit", exit_application)

window.mainloop()