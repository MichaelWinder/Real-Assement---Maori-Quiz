import random
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
        return "A Question will be displayed and you can pick from four " \
               "options.\nIf you choose the right answer you will receive a " \
               "point.\nIf Wrong then you won't get a point" \
               " and the correct answer will be displayed\n" \
               "Your total score will be shown at the end\nSo do well!"
    elif itype == "torf":
        return "A Question will be displayed and you can pick either True " \
               "or False.\nIf you choose the right answer you will receive a" \
               " point.\nIf Wrong then you won't get a point" \
               " and the correct answer will be displayed\n" \
               "Your total score will be shown at the end\nSo do well!"
    elif itype == "whole":
        return "A Question will be displayed and you have to type an answer." \
               "\nIf you type the right answer you will receive a point.\n" \
               "If Wrong then you won't get a point and the correct answer " \
               "will be displayed\nAll answers are only one word\n" \
               "Your total score will be shown at the end\nSo do well!"


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
                   command=lambda: [welcome.destroy(), multi_instructions(
                       mc_list)])
    multi.place(x=250, y=300, anchor='ne')
    torf = Button(welcome, text="True or False", font=(bse, 13), bg=btn,
                  command=lambda: [welcome.destroy(), torf_instructions(
                      tf_list)])
    torf.place(x=400, y=300, anchor='n')
    whole = Button(welcome, text="Whole Word", font=(bse, 13), bg=btn,
                   command=lambda: [welcome.destroy(),
                                    whole_word_instructions(ww_list)])
    whole.place(x=550, y=300, anchor='nw')
    result = Button(welcome, text="Results", font=(bse, 13), bg=btn,
                    command=lambda: [welcome.destroy(), results()])
    result.place(x=310, y=360, anchor='n')
    exit = Button(welcome, text="Exit", font=(bse, 13), bg=btn,
                  command=lambda: [save_questions("maori_quiz_questions.txt"),
                                   quit()])
    exit.place(x=490, y=360, anchor='n')
    mainloop()


def next_question(tk_screen):
    next_q_btn = Button(tk_screen, text="Next Question", font=(bse, 13),
                        bg=btn, command=lambda: tk_screen.destroy())
    next_q_btn.place(x=400, y=400, anchor=N)


def ans_check(tk_screen, answer, c_answer):
    if answer == c_answer:
        right = Label(tk_screen, text="CORRECT", bg=bgd, fg=c_ans,
                      font=(ttl, 35), relief="raised")
        right.place(x=400, y=160, anchor=N)
        global game_score
        game_score += 1
    elif answer != c_answer:
        wrong = Label(tk_screen, text="WRONG", bg=bgd, fg=w_ans,
                      font=(ttl, 35), relief="raised")
        wrong.place(x=400, y=160, anchor=N)
        correct_answer = Label(tk_screen, text=f"The Correct Answer was "
                                               f"{c_answer}", bg=bgd,
                               fg=txt, font=(bse, 14), relief="sunken")
        correct_answer.place(x=400, y=250, anchor=N)
    global game_questions
    game_questions += 1


def disable_btns(btn_list):
    for btn in btn_list:
        btn["state"] = DISABLED


def multi_instructions(ques):
    global game_score, game_questions
    game_score = 0
    game_questions = 0
    multi_i = Tk()
    multi_i.title("Maori Quiz!")
    multi_i.geometry("+2500+100")
    multi_i.minsize(800, 500)
    multi_i.resizable(False, False)
    multi_i.configure(bg='steel blue')
    # Creating the header
    box = Canvas(multi_i, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(multi_i, text="Multiple Choice Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(multi_i, text="Instructions", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=106, anchor=CENTER)
    Label(multi_i, text=instructions("multi"), bg=bgd, fg=txt,
          font=(bse, 15)).place(x=400, y=250, anchor=CENTER)
    Button(multi_i, text="Start", bg=btn, font=(bse, 15), command=lambda:
    multi_i.destroy()).place(x=400, y=400, anchor=N)
    multi_i.wait_window(multi_i)
    random.shuffle(ques)
    for question in ques:
        multi_choice(question)
    question_totals(game_score, game_questions)
    play_again()


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
                                                 ques.answer),
                                       next_question(multi),
                                       disable_btns(btn_list)])
    option_1.place(x=250, y=300, anchor=CENTER)
    option_2 = Button(multi, text=ques.options[1], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[1],
                                                 ques.answer),
                                       next_question(multi),
                                       disable_btns(btn_list)])
    option_2.place(x=350, y=300, anchor=CENTER)
    option_3 = Button(multi, text=ques.options[2], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[2],
                                                 ques.answer),
                                       next_question(multi),
                                       disable_btns(btn_list)])
    option_3.place(x=450, y=300, anchor=CENTER)
    option_4 = Button(multi, text=ques.options[3], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(multi, ques.options[3],
                                                 ques.answer),
                                       next_question(multi),
                                       disable_btns(btn_list)])
    option_4.place(x=550, y=300, anchor=CENTER)
    btn_list = [option_1, option_2, option_3, option_4]
    multi.wait_window(multi)


def torf_instructions(ques):
    global game_score, game_questions
    game_score = 0
    game_questions = 0
    torf_i = Tk()
    torf_i.title("Maori Quiz!")
    torf_i.geometry("+2500+100")
    torf_i.minsize(800, 500)
    torf_i.resizable(False, False)
    torf_i.configure(bg='steel blue')
    # Creating the header
    box = Canvas(torf_i, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(torf_i, text="True or False Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(torf_i, text="Instructions", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=106, anchor=CENTER)
    Label(torf_i, text=instructions("torf"), bg=bgd, fg=txt,
          font=(bse, 15)).place(x=400, y=250, anchor=CENTER)
    Button(torf_i, text="Start", bg=btn, font=(bse, 15), command=lambda:
    torf_i.destroy()).place(x=400, y=400, anchor=N)
    torf_i.wait_window(torf_i)
    random.shuffle(ques)
    for question in ques:
        t_or_f(question)
    question_totals(game_score, game_questions)
    play_again()


def t_or_f(ques):
    torf = Tk()
    torf.title("Maori Quiz!")
    torf.geometry("+2500+100")
    torf.minsize(800, 500)
    torf.resizable(False, False)
    torf.configure(bg='steel blue')
    # Creating the header
    box = Canvas(torf, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(torf, text="True or False Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    question_l = Label(torf, text=ques.text, bg=bgd, fg=txt,
                       font=(ttl, 25))
    question_l.place(x=400, y=106, anchor=CENTER)
    option_1 = Button(torf, text=ques.options[0], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(torf, ques.options[0],
                                                 ques.answer),
                                       next_question(torf),
                                       disable_btns(btn_list)])
    option_1.place(x=300, y=300, anchor=CENTER)
    option_2 = Button(torf, text=ques.options[1], font=(bse, 13), bg=btn,
                      command=lambda: [ans_check(torf, ques.options[1],
                                                 ques.answer),
                                       next_question(torf),
                                       disable_btns(btn_list)])
    option_2.place(x=500, y=300, anchor=CENTER)
    btn_list = [option_1, option_2]
    torf.wait_window(torf)


def whole_word_instructions(ques):
    global game_score, game_questions
    game_score = 0
    game_questions = 0
    whole_i = Tk()
    whole_i.title("Maori Quiz!")
    whole_i.geometry("+2500+100")
    whole_i.minsize(800, 500)
    whole_i.resizable(False, False)
    whole_i.configure(bg='steel blue')
    # Creating the header
    box = Canvas(whole_i, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(whole_i, text="Whole Word Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(whole_i, text="Instructions", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=106, anchor=CENTER)
    Label(whole_i, text=instructions("whole"), bg=bgd, fg=txt,
          font=(bse, 15)).place(x=400, y=250, anchor=CENTER)
    Button(whole_i, text="Start", bg=btn, font=(bse, 15), command=lambda:
    whole_i.destroy()).place(x=400, y=400, anchor=N)
    whole_i.wait_window(whole_i)
    random.shuffle(ques)
    for question in ques:
        whole_word(question)
    question_totals(game_score, game_questions)
    play_again()


def whole_word(ques):
    whole = Tk()
    whole.title("Maori Quiz!")
    whole.geometry("+2500+100")
    whole.minsize(800, 500)
    whole.resizable(False, False)
    whole.configure(bg='steel blue')
    ans_var = StringVar()
    ans_var.set("")
    # Creating the header
    box = Canvas(whole, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(whole, text="Whole Word Questions!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    question_l = Label(whole, text=ques.text, bg=bgd, fg=txt,
                       font=(ttl, 25))
    question_l.place(x=400, y=106, anchor=CENTER)
    enter = Label(whole, text="Enter Answer Below", bg=bgd, fg=txt,
                  font=(ttl, 25))
    enter.place(x=400, y=320, anchor=S)
    user_answer = Entry(whole, bg=bgd, fg=txt, font=(bse, 20),
                        textvariable=ans_var)
    user_answer.place(x=400, y=320, anchor=N)
    user_answer.focus()
    enter_btn = Button(whole, text="Enter", font=(bse, 13), bg=btn,
                       command=lambda: [ans_check(whole, ans_var.get().title(),
                                                  ques.answer),
                                        next_question(whole),
                                        disable_btns(btn_list)])
    enter_btn.place(x=400, y=360, anchor=N)
    btn_list = [enter_btn]
    whole.wait_window(whole)


def play_a_btns(tk_screen):
    tk_screen: Tk
    option_1 = Button(tk_screen, text="Multi Choice", font=(bse, 13), bg=btn,
                      command=lambda: [tk_screen.destroy(),
                                       multi_instructions(mc_list)])
    option_1.place(x=250, y=360, anchor=CENTER)
    option_2 = Button(tk_screen, text="True or False", font=(bse, 13), bg=btn,
                      command=lambda: [tk_screen.destroy(), torf_instructions(
                          tf_list)])
    option_2.place(x=400, y=360, anchor=CENTER)
    option_3 = Button(tk_screen, text="Whole Word", font=(bse, 13), bg=btn,
                      command=lambda: [tk_screen.destroy(),
                                       whole_word_instructions(ww_list)])
    option_3.place(x=550, y=360, anchor=CENTER)


def play_again():
    play_a = Tk()
    play_a.title("Maori Quiz!")
    play_a.geometry("+2500+100")
    play_a.minsize(800, 500)
    play_a.resizable(False, False)
    play_a.configure(bg='steel blue')
    # Creating the header
    box = Canvas(play_a, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    Label(play_a, text="Play Again?", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(play_a, text=f"You Scored {game_score}/{game_questions}!", bg=bgd,
          fg=txt, font=(ttl, 25)).place(x=400, y=120, anchor=CENTER)
    Label(play_a, text="Would you like to play again\nor receive your total "
                       "results", bg=bgd, fg=txt, font=(ttl, 25)).place(
        x=400, y=210, anchor=CENTER)
    option_1 = Button(play_a, text="Play Again", font=(bse, 13), bg=btn,
                      command=lambda: [play_a_btns(play_a), disable_btns(
                          btn_list)])
    option_1.place(x=300, y=300, anchor=CENTER)
    option_2 = Button(play_a, text="Results", font=(bse, 13), bg=btn,
                      command=lambda: [play_a.destroy(), results()])
    option_2.place(x=500, y=300, anchor=CENTER)
    btn_list = [option_1, option_2]
    play_a.wait_window(play_a)


def question_totals(game_s, game_q):
    global total_score, total_questions
    total_score += game_s
    total_questions += game_q


def results():
    result = Tk()
    result.title("Maori Quiz!")
    result.geometry("+2500+100")
    result.minsize(800, 500)
    result.resizable(False, False)
    result.configure(bg='steel blue')
    # Creating the header
    box = Canvas(result, width=800, height=75)
    box.place(x=0, y=0, anchor=NW)
    box.create_rectangle(0, 0, 801, 76, fill=hed, outline=hed)
    box.pack()
    percentage = total_score/total_questions * 100
    Label(result, text="Results!", bg=hed,
          fg=txt, font=(ttl, 34)).place(x=401, y=5, anchor='n')
    Label(result, text=f"You Scored {total_score}/{total_questions} in "
                       f"total!\nThat's {percentage}%", bg=bgd, fg=txt,
          font=(ttl, 25)).place(x=400, y=150, anchor=CENTER)
    if percentage < 30:
        Label(result, text="You are quite bad actually, Study More!", bg=bgd,
              fg=txt, font=(ttl, 25)).place(x=400, y=230, anchor=CENTER)
    elif percentage < 75:
        Label(result, text="You are on the right track, Good Try!", bg=bgd,
              fg=txt, font=(ttl, 25)).place(x=400, y=230, anchor=CENTER)
    else:
        Label(result, text="WOW you did really well, Good Job!", bg=bgd,
              fg=txt, font=(ttl, 25)).place(x=400, y=230, anchor=CENTER)
    Label(result, text="Thank you for playing my Maori Quiz!",
          bg=bgd, fg=txt, font=(ttl, 25)).place(x=400, y=300, anchor=CENTER)
    option_1 = Button(result, text="Exit", font=(bse, 13),
                      bg=btn, command=lambda: [result.destroy(), quit()])
    option_1.place(x=400, y=380, anchor=CENTER)
    result.wait_window(result)


# Main Routine
q_list: list[Questions] = [Questions("MC", "What is Ethan",
                                     ["Wrong", "Right", "Dumbo", "Smarto"],
                                     "Wrong"),
                           Questions("MC", "What is Thomas",
                                     ["Wrong", "Right", "Dumbo", "Smarto"],
                                     "Dumbo"),
                           Questions("MC", "What is James",
                                     ["Wrong", "Right", "Dumbo", "Smarto"],
                                     "Wrong"),
                           Questions("MC", "What is Lucas",
                                     ["Wrong", "Right", "Dumbo", "Smarto"],
                                     "Dumbo"),
                           Questions("MC", "What is Michael",
                                     ["Wrong", "Right", "Dumbo", "Smarto"],
                                     "Smarto"),
                           Questions("TF", "Is Ethan Wrong", ["True", "False"],
                                     "True"),
                           Questions("TF", "Is Ethan Wong", ["True", "False"],
                                     "False"),
                           Questions("TF", "Is Thomas", ["True", "False"],
                                     "False"),
                           Questions("TF", "Isn't Lucas", ["True", "False"],
                                     "True"),
                           Questions("WW", "Is Ethan actually cool tho", [],
                                     "Yes"),
                           Questions("WW", "Is Thomas actually cool tho", [],
                                     "Yes"),
                           Questions("WW", "Is Lucas actually cool tho", [],
                                     "Yes"),
                           Questions("WW", "Is James actually cool tho", [],
                                     "No")]
mc_list = []
tf_list = []
ww_list = []
game_score = 0
game_questions = 0
total_score = 0
total_questions = 0

while True:
    menu()
