import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def display_result(self, user_choice, computer_choice, winner):
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
        else:
            print("You lose!")

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")

        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)

            self.display_result(user_choice, computer_choice, winner)

            if winner == "user":
                self.user_score += 1
            elif winner == "computer":
                self.computer_score += 1

            print(f"\nScores - You: {self.user_score}, Computer: {self.computer_score}")

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for playing! Goodbye!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()

