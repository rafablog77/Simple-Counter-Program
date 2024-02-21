# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from platform import system
from tkinter import Button, Canvas, PhotoImage, Tk

OUTPUT_PATH = Path(__file__).parent
OS_NAME = system()
assets_path = None
if OS_NAME == "Windows":
  assets_path = OUTPUT_PATH / Path(r"assets\frame0")
else:
  assets_path = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)

count = 0
def increase():
  global count
  count += 1
  canvas.itemconfig(tagOrId=counter_text, text=count)
def decrease():
  global count
  count -= 1
  canvas.itemconfig(tagOrId=counter_text, text=count)

window = Tk()

window.geometry("236x102")
window.configure(bg = "#F8FDFF")
window.title("Simple Counter")


canvas = Canvas(
    window,
    bg = "#F8FDFF",
    height = 102,
    width = 236,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
counter_text = canvas.create_text(
    92.0,
    25.0,
    anchor="nw",
    text="0",
    fill="#000000",
    font=("Inter", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=increase,
    relief="flat"
)
button_1.place(
    x=165.0,
    y=25.0,
    width=53.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=decrease,
    relief="flat"
)
button_2.place(
    x=19.0,
    y=25.0,
    width=53.0,
    height=53.0
)

window.resizable(False, False)
window.mainloop()