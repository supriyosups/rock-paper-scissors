import random
import tkinter as tk
from tkinter import messagebox

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    winner = determine_winner(player_choice, computer_choice)
    
    result = f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{winner}"
    messagebox.showinfo("Rock-Paper-Scissors", result)

def create_gui():
    window = tk.Tk()
    window.title("Rock-Paper-Scissors")
    
    label = tk.Label(window, text="Choose your move:")
    label.pack(pady=10)
    
    button_frame = tk.Frame(window)
    button_frame.pack()
    
    rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_game('rock'))
    rock_button.grid(row=0, column=0, padx=10, pady=5)
    
    paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_game('paper'))
    paper_button.grid(row=0, column=1, padx=10, pady=5)
    
    scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_game('scissors'))
    scissors_button.grid(row=0, column=2, padx=10, pady=5)
    
    window.mainloop()

create_gui()
