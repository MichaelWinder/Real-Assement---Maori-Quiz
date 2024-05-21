from tkinter import *

# Colours
bgd = "steel blue"
hed = "chocolate2"
btn = "peach puff"
txt = "white"
c_ans = "lime green"
w_ans = "red"
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


def set_lists():
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
    set_lists()
    welcome = Tk()
    welcome.title("Maori Quiz!")
    welcome.geometry("+2500+100")
    welcome.minsize(800, 500)
    welcome.resizable(False, False)
    welcome.configure(bg='steel blue')
    # Creating the header
    box = Canvas(welcome, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    # Text Labels for Welcome Screen
    Label(welcome, text="Welcome to the Maori Quiz!", bg=hed, fg=txt,
          font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(welcome, text="Instructions", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=106, anchor=CENTER)
    Label(welcome, text=instructions("welcome"), bg=bgd, fg=txt,
          font=(bse, 12)).place(x=400, y=200, anchor=CENTER)
    # Buttons for Welcome Screen
    multi = Button(welcome, text="Multiple Choice", font=(bse, 13), bg=btn,
                   command=lambda: [welcome.destroy(), multi_list(mc_list)])
    multi.place(x=250, y=300, anchor='ne')
    torf = Button(welcome, text="True or False", font=(bse, 13), bg=btn,
                  command=lambda: [welcome.destroy(), "true_or_false()"])
    torf.place(x=400, y=300, anchor='n')
    whole = Button(welcome, text="Whole Word", font=(bse, 13), bg=btn,
                   command=lambda: [welcome.destroy(), "whole_word()"])
    whole.place(x=550, y=300, anchor='nw')
    results = Button(welcome, text="Results", font=(bse, 13), bg=btn,
                     command=lambda: [welcome.destroy(), "results()"])
    results.place(x=310, y=360, anchor='n')
    exit = Button(welcome, text="Exit", font=(bse, 13), bg=btn,
                  command=lambda: quit())
    exit.place(x=490, y=360, anchor='n')
    mainloop()


def multi_list(ques):
    for question in ques:
        multi_choice(question)


def next_question(tk_screen):
    next_q_btn = Button(tk_screen, text="Next Question", font=(bse, 13),
                        bg=btn, command=lambda: tk_screen.destroy())
    next_q_btn.place(x=400, y=400, anchor=N)


def ans_check(tk_screen, answer, c_answer):
    if answer == c_answer:
        right = Label(tk_screen, text="CORRECT", bg=bgd, fg=c_ans,
                      font=(ttl, 35), relief="raised")
        right.place(x=400, y=160, anchor=N)
    elif answer != c_answer:
        wrong = Label(tk_screen, text="WRONG", bg=bgd, fg=w_ans,
                      font=(ttl, 35), relief="raised")
        wrong.place(x=400, y=160, anchor=N)
        correct_answer = Label(tk_screen, text=f"The Correct Answer was "
                                               f"{c_answer}", bg=bgd,
                               fg=txt, font=(bse, 14), relief="sunken")
        correct_answer.place(x=400, y=250, anchor=N)


def disable_btns(btn_list):
    for btn in btn_list:
        btn["state"] = DISABLED


def multi_choice(ques):
    multi = Tk()
    multi.title("Maori Quiz!")
    multi.geometry("+2500+100")
    multi.minsize(800, 500)
    multi.resizable(False, False)
    multi.configure(bg='steel blue')
    # Creating the header
    box = Canvas(multi, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(multi, text="Multiple Choice Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    question_l = Label(multi, text=ques.text, bg=bgd, fg=txt,
                       font=(ttl, 25))
    question_l.place(x=400, y=106, anchor=CENTER)
    option_1 = Button(multi, text=ques.options[0], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[0],
                                       ques.answer), next_question(multi),
                                       disable_btns(btn_list)])
    option_1.place(x=250, y=300, anchor=CENTER)
    option_2 = Button(multi, text=ques.options[1], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[1],
                                       ques.answer), next_question(multi),
                                       disable_btns(btn_list)])
    option_2.place(x=350, y=300, anchor=CENTER)
    option_3 = Button(multi, text=ques.options[2], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[2],
                                       ques.answer), next_question(multi),
                                       disable_btns(btn_list)])
    option_3.place(x=450, y=300, anchor=CENTER)
    option_4 = Button(multi, text=ques.options[3], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[3],
                                       ques.answer), next_question(multi),
                                       disable_btns(btn_list)])
    option_4.place(x=550, y=300, anchor=CENTER)
    btn_list = [option_1, option_2, option_3, option_4]
    multi.wait_window(multi)


# Main Routine
q_list = []
mc_list = []
tf_list = []
ww_list = []
Questions("MC", "What is Ethan?", ["Wrong", "Right", "Dumbo", "Smarto"],
          "Wrong")
Questions("MC", "What is Thomas", ["Wrong", "Right", "Dumbo", "Smarto"],
          "Dumbo")
menu()
