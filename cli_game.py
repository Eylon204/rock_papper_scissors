from game_logic import get_computer_choice, determine_winner, get_scores

def play_cli():
    """משחק CLI עם ניקוד"""
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(f"\n{result}\n")

        scores = get_scores()
        print(f"Scores: You - {scores['player']}, Computer - {scores['computer']}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break