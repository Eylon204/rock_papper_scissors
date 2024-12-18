from cli_game import play_cli

def main():
    """בחירת גרסה (CLI או GUI)"""
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose a version to play:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        from cli_game import play_cli
        play_cli()
    elif choice == "2":
        from gui_game import play_gui
        play_gui()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()