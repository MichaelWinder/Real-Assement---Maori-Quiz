from tkinter import *

root = Tk()

root.title("Maori Quiz!")

root.geometry("+2500+100")
root.minsize(800, 500)
root.resizable(False, False)
root.configure(bg='steel blue')
Label(root, text="Welcome to the Maori Quiz", bg="steel blue",
      fg="white", font=("Arial Black", 40, "bold")).grid(row=0, column=3)
mainloop()
