from tkinter import *


def instructions(itype):
    if itype == "welcome":
        return "Click on one of the five buttons below.\nThe " \
               "Multiple choice button gives 10 multiple choice questions.\n" \
               "The True or False button gives 10 True or false questions.\n" \
               "The Whole word button gives 10 questions that require a " \
               "whole word answer.\nClick on Results to get your results.\n" \
               "Click on Exit to end the program."
    elif itype == "multi":
        pass
    elif itype == "trueorfalse":
        pass
    elif itype == "whole":
        pass


welcome = Tk()

welcome.title("Maori Quiz!")

welcome.geometry("+2500+100")
welcome.minsize(800, 500)
welcome.resizable(False, False)
welcome.configure(bg='steel blue')
# Text Labels for Welcome Screen
Label(welcome, text="Welcome to the Maori Quiz!", bg="chocolate2",
      fg="white", font=("Arial Black", 40, "bold")).grid(row=0,
                                                         columnspan=3)
Label(welcome, text="Instructions", bg="steel blue", fg="white",
      font=("Arial Black", 25, "bold")).grid(row=1, column=1, pady=10)
Label(welcome, text=instructions("welcome"), bg="steel blue", fg="white",
      font=("Arial Black", 10)).grid(row=2, column=1, pady=0)
mainloop()
