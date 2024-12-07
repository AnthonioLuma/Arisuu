

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import database as db

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\TaysaMarkAnthony(Stu\Desktop\Arisuu\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    800.0,
    fill="#2E4351",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    374.0,
    481.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    150.0,
    image=image_image_2
)

canvas.create_rectangle(
    620.0,
    261.0,
    1135.0,
    572.0,
    fill="#97BCC7",
    outline="")

canvas.create_text(
    640.0,
    285.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    640.0,
    379.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=663.0,
    y=477.0,
    width=406.0,
    height=46.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    872.0,
    343.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Arial",20)
)
entry_1.place(
    x=640.0,
    y=321.0,
    width=464.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    872.0,
    439.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Arial",20),
    show="*"
)
entry_2.place(
    x=640.0,
    y=417.0,
    width=464.0,
    height=43.0
)
window.resizable(False, False)
window.mainloop()
