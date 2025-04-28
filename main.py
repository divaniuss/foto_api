import tkinter as tk
from PIL import Image, ImageTk

from getImg import getimg

root = tk.Tk()
root.title("Foto:")
root.geometry("500x600")

entry = tk.Entry(root)
entry.pack(pady=5)

img_label = tk.Label(root)
img_label.pack()

current_photo = None

def get():
    global current_photo
    a = entry.get()
    w,h = getimg(a)
    h += 70
    image = Image.open("img.jpeg")
    root.geometry(f"{w}x{h}")
    current_photo = ImageTk.PhotoImage(image)
    img_label.config(image=current_photo)

tk.Button(root, text="показать", command = get).pack(pady=5)

root.mainloop()
