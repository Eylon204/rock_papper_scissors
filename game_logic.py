import os
import json
import random

SCORE_FILE = "data/scores.json"

# יצירת תיקייה וקובץ ניקוד אם הם לא קיימים
if not os.path.exists(SCORE_FILE):
    os.makedirs("data", exist_ok=True)  # יצירת תיקיית data אם היא לא קיימת
    with open(SCORE_FILE, "w") as file:
        json.dump({"player": 0, "computer": 0}, file)

def get_computer_choice():
    """מחשב בוחר מהלך"""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """קובע מי ניצח"""
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        update_scores("player")
        return "You win!"
    else:
        update_scores("computer")
        return "Computer wins!"

def update_scores(winner):
    """מעדכן את הניקוד"""
    with open(SCORE_FILE, "r") as file:
        scores = json.load(file)

    scores[winner] += 1

    with open(SCORE_FILE, "w") as file:
        json.dump(scores, file)

def get_scores():
    """מחזיר את הניקוד הנוכחי"""
    with open(SCORE_FILE, "r") as file:
        return json.load(file)