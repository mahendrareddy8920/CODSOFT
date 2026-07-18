import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=" * 50)
print("      ROCK - PAPER - SCISSORS GAME")
print("=" * 50)
print("Rules:")
print("• Rock beats Scissors")
print("• Scissors beat Paper")
print("• Paper beats Rock")
print("=" * 50)

while True:
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice.capitalize()}")
    print(f"Computer chose : {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("\n🤝 It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\n🎉 Congratulations! You Win!")
        user_score += 1

    else:
        print("\n💻 Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("-" * 20)
    print(f"You       : {user_score}")
    print(f"Computer  : {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n========== FINAL SCORE ==========")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        if user_score > computer_score:
            print("\n🏆 Overall Winner: You!")
        elif computer_score > user_score:
            print("\n🏆 Overall Winner: Computer!")
        else:
            print("\n🤝 The Match Ends in a Tie!")

        print("\nThank you for playing!")
        break
