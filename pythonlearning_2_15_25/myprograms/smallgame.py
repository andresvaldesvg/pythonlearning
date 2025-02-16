import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb  # Import ttkbootstrap for enhanced styling

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def on_click(row, col):
    global current_player
    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        elif all(board[row][col] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

def create_grid_lines():
    for i in range(1, 3):
        canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=2)
        canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=2)

root = tb.Window(themename="journal")  # Use ttkbootstrap Window with a theme
# The theme is set to "flatly" in the line above
root.title("Tic Tac Toe")

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0, rowspan=3, columnspan=3)
create_grid_lines()

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=('Helvetica', 20), width=5, height=2,
                           command=lambda row=row, col=col: on_click(row, col))
        button_window = canvas.create_window(col * 100 + 50, row * 100 + 50, window=button)
        buttons[row][col] = button

reset_button = tk.Button(root, text="Reset", font=('Helvetica', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()
