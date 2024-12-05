import tkinter as tk
from tkinter import *
from tkinter import messagebox
from sample import relative_to_assets



login_window = tk.Tk()
login_window.title("Arisu")
login_window.geometry("800x600")
login_window.configure(bg="#97bcc7")
icon = PhotoImage(file =relative_to_assets("pngegg.png"))
login_window.iconphoto(False,icon)

csh_btn= tk.Button (login_window, text= "Login" ,font= ("Arial",13),width=30)
stk_btn= tk.Button (login_window, text= "Sign Up" ,font= ("Arial",13),width=30)
rm_btn= tk.Button (login_window, text= "Login" ,font= ("Arial",13),width=30)
sgn_btn= tk.Button (login_window, text= "Sign Up" ,font= ("Arial",13),width=30)





csh_btn.pack(pady=20)
stk_btn.pack(pady=20)
rm_btn.pack(pady=20)
sgn_btn.pack(pady=20)

 



login_window.mainloop()