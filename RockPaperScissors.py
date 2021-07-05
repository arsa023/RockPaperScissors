import random

# ------------------------------------


input("Welcome to the game Rock,Paper,Scissors.Press Enter to start.")
def game():
user_score = 0
ai_score = 0

while True:
        user_score = 0
        ai_score = 0
        user_choice = input("Rock, Paper or Scissors? ").lower()    # user enters his choice
        random_num = random.randint(0, 2)  # randomly choosing one >  0-rock 1- paper - 2- scissors

        while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
            user_choice = input("Invalid input, please try again: ").lower()
        if random_num == 0:
            ai_choice = "rock"
        elif random_num == 1:
            ai_choice = "paper"
        elif random_num == 2:
            ai_choice = "scissors"

        print()
        print("Your choice: ", user_choice)
        print("Ai choice: ", ai_choice)
        print()

        if user_choice == "rock":
            if ai_choice == "rock":
                print("Its a tie")
            if ai_choice == "paper":
                print("Computer Wins")
                ai_score += 1
            if ai_choice == "scissors":
                print("User Wins")
                user_score += 1
        elif user_choice == "paper":
            if ai_choice == "rock":
                print("User Wins")
                user_score += 1
            if ai_choice == "paper":
                print("Its a tie")
            if ai_choice == "scissors":
                print("Computer Wins")
                ai_score += 1
        elif user_choice == "scissors":
            if ai_choice == "rock":
                print("Computer Wins")
                ai_score += 1
            if ai_choice == "paper":
                print("User Wins")
                user_score += 1
            if ai_choice == "scissors":
                print("Its a tie")
        print()
        print("U have", user_score, "wins")
        print("Computer have", ai_score, "wins")
        print()

        if user_score == 10:
            print("U won!!!")
            repeat = input("Play again?(Y/N)").lower()
            while repeat != "n" and repeat != "y":
                repeat = input("invalid input, please try again! Y or N: ").lower()
            if repeat == "y":
                game()
            elif repeat == "n":
                break
        elif ai_score == 10:
            print("Game Over!!!")
            repeat = input("Play again?(Y/N)").lower()
            while repeat != "n" and repeat != "y":
                repeat = input("invalid input, please try again! Y or N: ").lower()
            if repeat == "y":
               game()

            elif repeat == "n":
                break

        print("\n_____________________\n")


