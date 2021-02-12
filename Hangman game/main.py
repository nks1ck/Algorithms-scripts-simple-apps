def hangman(word):
    """Main game loop"""
    wrong = 0  # Attempts, when user missed up
    stages = ["",
              "___________      ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
              ]
    letters = list(word)
    board = ["_"] * len(word)
    win = False  # Check for win

    print("Welcome to the Hangman game!")

    while wrong < len(stages) - 1:
        print("\n")
        guess = "Enter a letter: "
        char = input(guess)

        if char in letters:
            founded = letters.index(char)  # Founded char
            board[founded] = char
            letters[founded] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        mistakes = wrong + 1
        print("\n".join(stages[0: mistakes]))
        if "_" not in board:
            print(f"You won! The hidden word was - {word}")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print(f"You've lost! The hiddew word was - {word}")


hangman("котик")
