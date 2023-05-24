import tkinter as tk


class GFrame:
    def __init__(self, x, y):
        self.x = x
        self.y = y


root = tk.Tk()
# root.iconbitmap("./stuff/icon.ico")
root.title("Tkinter Window Demo - Center")
root.geometry("500x300+50+50")
root.resizable(False, False)

label = tk.Label(root, text="PIPI POPO", font=("Arial", 18))
label.pack(padx=10, pady=10)

# textbox = tk.Text(root, height=3, font=("Arial", 16))
# textbox.pack(padx=10, pady=10)
button = tk.Button(root, text="clicke", font=("Arial", 16))
button.pack(padx=10, pady=10)

frame = tk.Frame(root)
columns = 2
for column in range(columns):
    frame.columnconfigure(column, weight=1)


root.mainloop()
