from tkinter import *

# Colours
bgd = "steel blue"
hed = "chocolate2"
btn = "peach puff"
txt = "white"
# Fonts
ttl = "Arial Black"
bse = "Arial"
bld = "Bold"


class Questions:
    def __init__(self, question_type, text, options, answer):
        self.question_type = question_type
        self.text = text
        self.options = options
        self.answer = answer
        q_list.append(self)
        for question in q_list:
            if question.question_type == "MC":
                mc_list.append(question)
        for question in q_list:
            if question.question_type == "TF":
                tf_list.append(question)
        for question in q_list:
            if question.question_type == "WW":
                ww_list.append(question)


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


def menu():
    welcome = Tk()

    welcome.title("Maori Quiz!")

    welcome.geometry("+2500+100")
    welcome.minsize(800, 500)
    welcome.resizable(False, False)
    welcome.configure(bg='steel blue')
    # Text Labels for Welcome Screen
    box = Canvas(welcome, bg=hed, width=800, height=200)\
    box.place(x=0, y=500, anchor=NW)
    square = box.create_rectangle(0, 500, 800, 300)
#    Label(welcome, text="Welcome to the Maori Quiz!", bg=hed,
 #         fg=txt, font=(ttl, 40)).place(x=0, y=0)
    Label(welcome, text="Instructions", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=106, anchor=CENTER)
    Label(welcome, text=instructions("welcome"), bg=bgd, fg=txt,
          font=(bse, 12)).place(x=400, y=200, anchor=CENTER)
    # Buttons for Welcome Screen
    multi = Button(welcome, text="Multiple Choice", font=(bse, 13), bg=btn,
                   command=lambda: [multi_choice(), welcome.destroy()])
    multi.place(x=250, y=300, anchor='ne')
    torf = Button(welcome, text="True or False", font=(bse, 13), bg=btn,
                  command=lambda: ["true_or_false()", welcome.destroy()])
    torf.place(x=400, y=300, anchor='n')
    whole = Button(welcome, text="Whole Word", font=(bse, 13), bg=btn,
                   command=lambda: ["whole_word()", welcome.destroy()])
    whole.place(x=550, y=300, anchor='nw')
    results = Button(welcome, text="Results", font=(bse, 13), bg=btn,
                     command=lambda: ["results()", welcome.destroy()])
    results.place(x=310, y=360, anchor='n')
    exit = Button(welcome, text="Exit", font=(bse, 13), bg=btn,
                  command=lambda: quit())
    exit.place(x=490, y=360, anchor='n')
    mainloop()


def multi_choice():
    multi = Tk()

    multi.title("Maori Quiz!")

    multi.geometry("+2500+100")
    multi.minsize(800, 500)
    multi.resizable(False, False)
    multi.configure(bg='steel blue')
    Label(multi, text="Multiple Choice Questions!", bg=hed,
          fg=txt, font=(ttl, 40)).place(x=0, y=0)


# Main Routine
q_list = []
mc_list = []
tf_list = []
ww_list = []

Questions("MC", "What is Ethan?", ["Wrong", "Right", "Dumbo", "Smarto"],
          "Wrong")


menu()