import tkinter as tk
from PIL import Image, ImageTk

from getDog import getimg

root = tk.Tk()
root.title("Bobik:")
root.geometry("500x600")

img_label = tk.Label(root)
img_label.pack()

current_photo = None

def get():
    global current_photo
    getimg()
    image = Image.open("img.jpeg")
    image = image.resize((500, 500))
    current_photo = ImageTk.PhotoImage(image)
    img_label.config(image=current_photo)

tk.Button(root, text="еще", command = get).pack(pady=5)

root.mainloop()
