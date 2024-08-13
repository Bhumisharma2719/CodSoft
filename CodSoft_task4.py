import random
print("'Rock beats Scissor'")
print("'Paper beats rock'")
print("'Scissor beats paper'")
def game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        comp_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nComputer choose: {comp_choice}")

        if user_choice == comp_choice:
            print(f"Both players selected {user_choice}. Match tie!")
        elif user_choice == 'rock':
            if comp_choice == 'scissors':
                print("You win!")
            else:
                print("You lose.")
        elif user_choice == 'paper':
            if comp_choice == 'rock':
                print("You win!")
            else:
                print("You lose.")
        elif user_choice == 'scissors':
            if comp_choice == 'paper':
                print("You win!")
            else:
                print("You lose.")

game()