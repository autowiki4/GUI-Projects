import tkinter as tk
from tkinter import ttk,messagebox
# GUI to play tic-tac-toe

# function to check for the winner
def winner_determiner():
    # the nine boxes required to play the game
    global box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9
    # all conditions below test for victorious cases and change background to green (#0f0)

    # execute only if the buttons are not empty
    if box_1["text"] != '' and box_2["text"] != '' and box_3["text"] != '':
        if box_1["text"] == box_2["text"] and box_2["text"] == box_3["text"] and box_1["text"] == box_3["text"]:
            box_1.config(bg='#0f0')
            box_2.config(bg='#0f0')
            box_3.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_1["text"]} IS  THE WINNER!')
            start.destroy() # close game interface
            mainscreen() # return to welcome screen
    elif box_4["text"] != '' and box_5["text"] != '' and box_6["text"] != '':
        if box_4["text"] == box_5["text"] and box_5["text"] == box_6["text"] and box_4["text"] == box_6["text"]:
            box_4.config(bg='#0f0')
            box_5.config(bg='#0f0')
            box_6.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_4["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_7["text"] != '' and box_8["text"] != '' and box_9["text"] != '':
        if box_7["text"] == box_8["text"] and box_8["text"] == box_9["text"] and box_7["text"] == box_9["text"]:
            box_7.config(bg='#0f0')
            box_8.config(bg='#0f0')
            box_9.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_7["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_1["text"] != '' and box_5["text"] != '' and box_9["text"] != '':
        if box_1["text"] == box_5["text"] and box_5["text"] == box_9["text"] and box_1["text"] == box_9["text"]:
            box_1.config(bg='#0f0')
            box_5.config(bg='#0f0')
            box_9.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_1["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_3["text"] != '' and box_5["text"] != '' and box_7["text"] != '':
        if box_3["text"] == box_5["text"] and box_5["text"] == box_7["text"] and box_3["text"] == box_7["text"]:
            box_3.config(bg='#0f0')
            box_5.config(bg='#0f0')
            box_7.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_3["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_1["text"] != '' and box_4["text"] != '' and box_7["text"] != '':
        if box_1["text"] == box_4["text"] and box_4["text"] == box_7["text"] and box_1["text"] == box_7["text"]:
            box_1.config(bg='#0f0')
            box_4.config(bg='#0f0')
            box_7.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_1["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_2["text"] != '' and box_5["text"] != '' and box_8["text"] != '':
        if box_2["text"] == box_5["text"] and box_5["text"] == box_8["text"] and box_2["text"] == box_8["text"]:
            box_2.config(bg='#0f0')
            box_5.config(bg='#0f0')
            box_8.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_2["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()
    elif box_3["text"] != '' and box_6["text"] != '' and box_9["text"] != '':
        if box_3["text"] == box_6["text"] and box_6["text"] == box_9["text"] and box_3["text"] == box_9["text"]:
            box_3.config(bg='#0f0')
            box_6.config(bg='#0f0')
            box_9.config(bg='#0f0')
            messagebox.showinfo(title='CONGRATULATIONS!',message= f'PLAYER {box_3["text"]} IS  THE WINNER!')
            start.destroy()
            mainscreen()

# function to quit program
def quit_program():
    response = messagebox.askyesno('QUIT','Do you want to quit or tic-tac-toe?')
    # 1 represents yes
    if response == 1:
        # quit the interface instantly
        start.destroy()
        # 0 represents no
    elif response == 0:
        pass

# to restart if there is no winner
def restart_program():
    gamer_decision = messagebox.askyesno('RESTART', 'Do you need to restart?')
    # 1 represents yes
    if gamer_decision == 1:
        # quit the interface instantly
        start.destroy()
        mainscreen()
        # 0 represents no
    elif gamer_decision == 0:
        pass

# switch the turn when necessary
def switch_turn(button):
    global next_turn
    if button == 'X':
        next_turn = 'O'
    elif button == 'O':
        next_turn = 'X'
    turn_lbl.config(text=next_turn)

# determine text on button
def on_click(button):
    if button["text"] == '':
        # ensure the first button contains the starting player from choice.get()
        button.config(text= turn_lbl['text'])
        # move to function to determine the other buttons
        switch_turn(button["text"])
        # move to function to determine the winner so that winner is declared as soon as someone wins
        winner_determiner()
    else:
        pass

# MAIN GAME INTERFACE
def begin_game():
    global start
    start = tk.Tk()
    # title of GUI window
    start.title('TIC-TAC-TOE')
    entry.destroy()

    global  turn_lbl
    start_lbl = tk.Label(start,text='GAME TIME',font=('bahnschrift',15))
    # display the first player
    turn_lbl = tk.Label(start,text=choice.get(),font=('bahnschrift',15))

    # create the nine buttons
    global box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9
    box_1 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_1))  # command = lambda: ....whatever your function is
    box_2 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_2))
    box_3 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_3))
    box_4 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_4))
    box_5 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_5))
    box_6 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_6))
    box_7 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_7))
    box_8 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_8))
    box_9 = tk.Button(start, text='', font=('bahnschrift', 15), fg='#fff', bg='#000',width=7,height=3,command=lambda:on_click(box_9))

    # button to quit python program
    btn_quit_program = tk.Button(start,text='QUIT GAME', font=('bahnschrift', 15), height=1, width=20, fg='#fff',
                                      bg='#000', command=quit_program)

    # button to restart game if needed
    btn_restart_program = tk.Button(start,text='RESTART GAME', font=('bahnschrift', 15), height=1, width=20, fg='#fff',
                                      bg='#000', command=restart_program)


    # positioning
    start_lbl.grid(row=0,column=0,columnspan=3)
    turn_lbl.grid(row=1,column=0,columnspan=3)
    box_1.grid(row=2,column=0,padx=3,pady=3)
    box_2.grid(row=2,column=1,padx=3,pady=3)
    box_3.grid(row=2,column=2,padx=3,pady=3)
    box_4.grid(row=3,column=0,padx=3,pady=3)
    box_5.grid(row=3,column=1,padx=3,pady=3)
    box_6.grid(row=3,column=2,padx=3,pady=3)
    box_7.grid(row=4,column=0,padx=3,pady=3)
    box_8.grid(row=4,column=1,padx=3,pady=3)
    box_9.grid(row=4,column=2,padx=3,pady=3)
    btn_quit_program.grid(row=5,column=0,columnspan=3,padx=3,pady=3)
    btn_restart_program.grid(row=6, column=0, columnspan=3, padx=3, pady=3)

    winner_determiner()
    # to enable the GUI to run
    start.mainloop()

# function to initialize initial selection interface
def mainscreen():
    global entry
    # initate home screen to select an intial character (X or O)
    entry = tk.Tk()
    # title of GUI window
    entry.title('tic-tac-toe')

    # create label
    entry_lbl = tk.Label(entry,text='WELCOME TO TIC-TAC-TOE',font=('Bahnschrift',15),fg='#000')

    # pick choice
    pick_choice = tk.Label(entry,text='Choose X or O: ',font=('bahnschrift',15),fg='#000')

    # list of available starting characters
    players = ['X','O']

    # enable use of the variable everywhere
    global choice
    # store the string variable for the available options in the game
    choice = tk.StringVar()
    # provide dropbox to select values (GUI, values, variable store)
    drop_down_button = ttk.Combobox(entry,values=players,textvariable=choice)

    # determine the player who starts
    def starting_player():
        if choice.get() == 'X' or choice.get() == 'O':
            # tell python to head to the gama interface
            begin_game()
        else:
            # tell user to pick an option
            messagebox.showwarning(title='INVALID',message='Pick "X" or "O" to proceed to game interface')
    begin = tk.Button(entry,text='START',font=('bahnschrift',15),fg='#fff',bg='#000',command=starting_player)

    # Positioning of buttons
    entry_lbl.grid(row=0, column=0,columnspan=2)
    pick_choice.grid(row=1, column=0)
    drop_down_button.grid(row=1,column=1)
    begin.grid(row=2,column=0,columnspan=2)


    entry.mainloop()

mainscreen()
