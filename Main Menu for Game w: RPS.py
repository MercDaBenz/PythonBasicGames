import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

        
#Create Object
root = tk.Tk()

#Set geometry of window
root.geometry("350x350")

#Title set
root.title("Basic game apps")

def run_game():
    showinfo(
        title="Selected Game",
        message=selected_game.get()
        )
    
    if selected_game.get() == "Game 1":
        RPS()


        



def RPS():
    root1 = tk.Tk()
    root1.geometry("350x400")
    root1.title("Rock Paper Scissors")

    label1 = ttk.Label(root1,
               text ="Welcome!").pack()
    
    # Computer Value
    computer_value = {
            "0":"Rock",
            "1":"Paper",
            "2":"Scissor"
    }

    # If player selected rock
    def isrock():
            c_v = computer_value[str(random.randint(0,2))]
            if c_v == "Rock":
                    match_result = "Match Draw"
            elif c_v=="Scissor":
                    match_result = "Player Win"
            else:
                    match_result = "Computer Win"
            l4.config(text = match_result)
            l1.config(text = "Rock")
            l3.config(text = c_v)
            
    # If player selected paper
    def ispaper():
            c_v = computer_value[str(random.randint(0, 2))]
            if c_v == "Paper":
                    match_result = "Match Draw"
            elif c_v=="Scissor":
                    match_result = "Computer Win"
            else:
                    match_result = "Player Win"
            l4.config(text = match_result)
            l1.config(text = "Paper")
            l3.config(text = c_v)

    # If player selected scissor
    def isscissor():
            c_v = computer_value[str(random.randint(0,2))]
            if c_v == "Rock":
                    match_result = "Computer Win"
            elif c_v == "Scissor":
                    match_result = "Match Draw"
            else:
                    match_result = "Player Win"
            l4.config(text = match_result)
            l1.config(text = "Scissor")
            l3.config(text = c_v)
    
    # Add Labels, Frames and Button
    l1 = ttk.Label(root1,
		text = "Player",
		font = 10)

    l2 = ttk.Label(root1,
		text = " VS ",
		font = "normal 10 bold")

    l3 = ttk.Label(root1,
                   text = "Computer",
                   font = 10)

    l1.pack()
    l2.pack()
    l3.pack()

    l4 = ttk.Label(root1,
                    text = "",
                    font = "normal 20 bold",
                    #width = 15 ,
                    borderwidth = 2,
                    relief = "solid")
    l4.pack(pady = 20)

    frame1 = ttk.Frame(root1)
    frame1.pack()

    b1 = ttk.Button(root1, text = "Rock",
			command = isrock)

    b2 = ttk.Button(root1, text = "Paper",
			command = ispaper)

    b3 = ttk.Button(root1, text = "Scissor",
			command = isscissor)


    b1.pack(padx = 10, pady = 10)
    b2.pack(padx = 10, pady = 10)
    b3.pack(padx = 10, pady = 10)


    
    

    
selected_game= tk.StringVar()  
games = ((('Rock, Paper, Scissors'), 'Game 1'),(('Guess the Number'), 'Game 2'),(('Tic, Tac, Toe'), 'Game 3'))

#labels
label = ttk.Label(text="Please choose a game: ")
label.pack(fill='x', padx=5, pady=5)

for game in games:
    r = ttk.Radiobutton(
        root,
        text=game[0],
        value=game[1],
        variable=selected_game
    )
    r.pack(fill='x', padx=5, pady=5)

#button to confirm option
button = ttk.Button(
    root,
    text="Load game:",
    command=run_game)

button.pack(fill='x', padx=5, pady=5)


    
root.mainloop()
    
