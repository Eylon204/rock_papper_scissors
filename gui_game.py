import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game_logic import get_computer_choice, determine_winner

def play(player_choice, button):
    """מעבד את בחירת השחקן עם אנימציה ומציג את התוצאה"""
    # אפקט לחיצה (אנימציה קצרה)
    original_color = button["bg"]
    button.config(bg="yellow")
    button.after(200, lambda: button.config(bg=original_color))

    # עיבוד המשחק
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    result_text = f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}"
    messagebox.showinfo("Result", result_text)

def play_gui():
    """יוצר ממשק משתמש גרפי עם אייקונים ואפקטים"""
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    # טוען את האייקונים
    rock_img = ImageTk.PhotoImage(Image.open("assets/rock.png").resize((100, 100)))
    paper_img = ImageTk.PhotoImage(Image.open("assets/paper.png").resize((100, 100)))
    scissors_img = ImageTk.PhotoImage(Image.open("assets/scissors.png").resize((100, 100)))

    # כותרת המשחק
    tk.Label(root, text="Choose your move:", font=("Arial", 16)).pack(pady=20)

    # כפתורים עם אייקונים ואפקטים
    rock_button = tk.Button(root, image=rock_img, bg="lightgray", command=lambda: play("rock", rock_button))
    paper_button = tk.Button(root, image=paper_img, bg="lightgray", command=lambda: play("paper", paper_button))
    scissors_button = tk.Button(root, image=scissors_img, bg="lightgray", command=lambda: play("scissors", scissors_button))

    # סידור הכפתורים
    rock_button.pack(side=tk.LEFT, padx=20)
    paper_button.pack(side=tk.LEFT, padx=20)
    scissors_button.pack(side=tk.LEFT, padx=20)

    # שמירת התייחסות לתמונות
    root.mainloop()