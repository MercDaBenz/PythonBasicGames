import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Create Object
root = tk.Tk()

#Set geometry of window
root.geometry("500x500")

#Title set
root.title("Basic game apps")

def show_selected_game():
    showinfo(
        title='Game Chosen:',
        message=selected_game.get()
    )
    

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
    command=show_selected_game)

button.pack(fill='x', padx=5, pady=5)
    
root.mainloop()
    
