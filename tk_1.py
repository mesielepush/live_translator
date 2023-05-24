import tkinter as tk
from tkinter import messagebox


class window:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)

        self.menubar.add_cascade(menu=self.filemenu, label="Filesx")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="some shit", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(
            self.root,
            text="Show messsage box",
            font=("Arial", 15),
            variable=self.check_state,
        )
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(
            self.root, text="Show", font=("Arial", 18), command=self.show_messages
        )

        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_messages(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(
                title="Messsagex", message=self.textbox.get("1.0", tk.END)
            )

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "q":
            self.show_messages()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="should turn off everything?"):
            self.root.destroy()


window()
