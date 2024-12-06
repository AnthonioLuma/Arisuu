from tkinter import *
class Windows:

    def open_cashier_window(window):
    
        cashier_window = Toplevel(window)  # Create a new Toplevel window
        cashier_window.title("Cashier")
        cashier_window.geometry("800x600")  # Set size for the cashier window

        Label(cashier_window, text="Welcome to the Cashier!", font=("Times New Roman", 16)).pack(pady=20)

        # Button to close the Cashier window and reopen the main window
        close_button = Button(cashier_window, text="Done", command=lambda: (cashier_window.destroy(), window.deiconify()))
        close_button.pack(pady=20)

        # Optionally, you can also handle the window close event
        cashier_window.protocol("WM_DELETE_WINDOW", lambda: (cashier_window.destroy(), window.deiconify()))
    
    
    def open_inventory_window(main_window):
        inventory_window = Toplevel(main_window)  # Create a new Toplevel window
        inventory_window.title("Inventory")
        inventory_window.geometry("800x600")  # Set size for the inventory window

        Label(inventory_window, text="Welcome to the Inventory!", font=("Times New Roman", 16)).pack(pady=20)

        # Button to close the Inventory window and reopen the main window
        close_button = Button(inventory_window, text="Done", command=lambda: (inventory_window.destroy(), main_window.deiconify()))
        close_button.pack(pady=20)

        # Optionally, you can also handle the window close event
        inventory_window.protocol("WM_DELETE_WINDOW", lambda: (inventory_window.destroy(), main_window.deiconify()))

    
    def open_supply_window(main_window):
        supply_window = Toplevel(main_window)  # Create a new Toplevel window
        supply_window.title("Supply")
        supply_window.geometry("800x600")  # Set size for the supply window

        Label(supply_window, text="Welcome to the Supply!", font=("Times New Roman", 16)).pack(pady=20)

        # Button to close the Supply window and reopen the main window
        close_button = Button(supply_window, text="Done", command=lambda: (supply_window.destroy(), main_window.deiconify()))
        close_button.pack(pady=20)

        # Optionally, you can also handle the window close event
        supply_window.protocol("WM_DELETE_WINDOW", lambda: (supply_window.destroy(), main_window.deiconify()))