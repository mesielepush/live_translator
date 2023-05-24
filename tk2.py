import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


class FrontPage:
    def __init__(self, title, height, width, pad):
        self.root = tk.Tk()
        self.root.title = title
        self.root.geometry(f"{str(height)}x{str(width)}+{str(pad)}+{str(pad)}")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.root.bind("<KeyPress>", self.close_button)

        img = Image.open("stuff/title.png").convert("RGBA")

        self.x_root = int(self.root.winfo_geometry().split("x")[0])

        img2 = img.resize(
            (int(img.size[0] * 0.50), int(img.size[1] * 0.50)), Image.ANTIALIAS
        )
        img2 = img2.crop([25, 10, 400, 150])
        image = ImageTk.PhotoImage(img2)

        label = tk.Label(
            self.root,
            image=image,
            borderwidth=0,
            highlightthickness=0,
            padx=0,
            pady=0,
            bg="black",
        )
        label.place(relx=0.65, rely=0.15, anchor="center")

        # frame = tk.Label(self.root, borderwidth=0, highlightthickness=0, padx=0, pady=0)
        # frame.pack()
        # frame.place(anchor="center", relx=0.5, rely=0.5)
        # img = ImageTk.PhotoImage(Image.open("stuff/title.png"))

        self.root.mainloop()

    def close_button(self, event):
        if event.state == 12 and event.keysym == "q":
            self.root.destroy()

    def recording_loop():
        print("recording loop")

    def on_demand_recording():
        print("on demand recording")


FrontPage(title="pipi", height=600, width=600, pad=20)
