import random

# ===========================
# HANGMAN GAME - PART 1
# ===========================

# High Score
high_score = 1


# Player Statistics
games_played = 0
games_won = 0
games_lost = 0

# Hangman Drawings
HANGMAN = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

# Words by Difficulty
easy_words = [
    "book",
    "tree",
    "milk",
    "ball",
    "apple",
    "chair",
    "bread",
    "green",
    "phone",
    "water"
]

medium_words = [
    "python",
    "teacher",
    "library",
    "country",
    "holiday",
    "picture",
    "computer",
    "football",
    "hospital",
    "building"
]

hard_words = [
    "programming",
    "cybersecurity",
    "development",
    "artificial",
    "information",
    "application",
    "communication",
    "engineering",
    "technology",
    "intelligence"
]

# Instructions
def instructions():
    print("\n========== HOW TO PLAY ==========")
    print("1. Guess one letter at a time.")
    print("2. You have limited lives.")
    print("3. Correct Letter = +10 points")
    print("4. Wrong Letter = -5 points")
    print("5. Complete Word = +50 points")
    print("6. Easy Bonus = +100")
    print("7. Medium Bonus = +200")
    print("8. Hard Bonus = +300")
    print("9. Hint Penalty = -20 points")
    print("10. Win All Levels = +500 Bonus")
    print("=================================\n")

# Rank System
def get_rank(score):
    if score >= 1200:
        return "👑 HANGMAN MASTER ⭐⭐⭐⭐⭐"
    elif score >= 800:
        return "EXPERT ⭐⭐⭐⭐"
    elif score >= 500:
        return "GREAT ⭐⭐⭐"
    elif score >= 200:
        return "GOOD ⭐⭐"
    else:
        return "BEGINNER ⭐"

# Main Menu
def menu():
    print("\n====================================")
    print("         HANGMAN GAME")
    print("====================================")
    print("1. Play Game")
    print("2. Instructions")
    print("3. View High Score")
    print("4. Exit")
    print("====================================")

# Game Function (continued in Part 2)
def play_game():
    global high_score
    global games_played
    global games_won
    global games_lost

    player = input("\nEnter Player Name: ")

    print("\nSelect Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Choice: ")

    if choice == "1":
        words = easy_words
        lives = 6
        bonus = 100
        difficulty = "Easy"

    elif choice == "2":
        words = medium_words
        lives = 5
        bonus = 200
        difficulty = "Medium"

    else:
        words = hard_words
        lives = 4
        bonus = 300
        difficulty = "Hard"

    score = 0
    hint_used = False

    # -------------------------------
    # PART 2 - GAME LOGIC
    # -------------------------------

    games_played += 1

    word = random.choice(words).lower()

    guessed_word = ["_"] * len(word)
    guessed_letters = []

    wrong_guesses = 0
    max_wrong = lives

    while wrong_guesses < max_wrong and "_" in guessed_word:

        print("\n====================================")
        print("Player :", player)
        print("Difficulty :", difficulty)
        print("Score :", score)
        print("Lives :", "❤️" * (max_wrong - wrong_guesses))
        print(HANGMAN[wrong_guesses])

        print("Word :", " ".join(guessed_word))
        print("Guessed :", " ".join(guessed_letters))

        if difficulty != "Hard" and not hint_used:
            print("Type HINT to reveal one letter (-20 Points)")

        guess = input("Enter a letter : ").lower().strip()

        # Hint
        if guess == "hint":

            if difficulty == "Hard":
                print("Hints are not available in Hard mode.")
                continue

            if hint_used:
                print("Hint already used.")
                continue

            hint_used = True
            score -= 20

            for letter in word:
                if letter not in guessed_letters:
                    guess = letter
                    print("Hint Letter :", guess.upper())
                    break

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:

            print("Correct!")

            score += 10

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

        else:

            print("Wrong!")

            wrong_guesses += 1
            score -= 5

    # -------------------------
    # Result
    # -------------------------

    if "_" not in guessed_word:

        games_won += 1

        score += 50
        score += bonus

        if difficulty == "Hard":
            score += 500

        print("\nCongratulations!")
        print("You guessed the word:", word)

    else:

        games_lost += 1

        print(HANGMAN[6])

        print("\nGame Over!")
        print("Correct Word :", word)

    # -------------------------
    # FINAL SCORE & STATISTICS
    # -------------------------

    if score < 0:
        score = 0

    print("\n========================================")
    print("             GAME SUMMARY")
    print("========================================")
    print("Player Name       :", player)
    print("Difficulty        :", difficulty)
    print("Final Score       :", score)
    print("Games Played      :", games_played)
    print("Games Won         :", games_won)
    print("Games Lost        :", games_lost)
    print("Hint Used         :", "Yes" if hint_used else "No")
    print("Player Rank       :", get_rank(score))
    print("========================================")

    if score > high_score:
        high_score = score
        print("🎉 NEW HIGH SCORE!")

    print("Current High Score:", high_score)

# ===========================
# MAIN PROGRAM
# ===========================

while True:

    menu()

    option = input("Enter your choice: ")

    if option == "1":
        play_game()

    elif option == "2":
        instructions()

    elif option == "3":
        print("\n========== HIGH SCORE ==========")
        print("High Score :", high_score)
        print("Games Played :", games_played)
        print("Games Won :", games_won)
        print("Games Lost :", games_lost)
        print("================================")

    elif option == "4":
        print("\nThank you for playing Hangman!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    again = input("\nReturn to Main Menu? (Y/N): ").lower()

    if again != "y":
        print("\nThanks for playing!")
        print("Final High Score:", high_score)
        break