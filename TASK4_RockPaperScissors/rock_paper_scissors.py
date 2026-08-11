import random
def get_computer_choice():
    return random.choice(['Rock' , 'Paper' , 'Scissors'])
def determine_winner(user , computer):
     if user == computer:
        return "tie"
     elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
     else:
        return "computer"
def play_game():
    print("Rock , Paper , Scissors")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("ENTER 'Rock' , 'Paper' , 'Scissors'")

        if user_choice not in ['Rock', 'Paper', 'Scissors']:
         print("Invalid choice. Try again.")
        continue      
computer_choice = get_computer_choice()

if winner == "tie":
            print("It's a tie!")
elif winner == "user":
            print("You win this round!")
            user_score += 1
else:
        print("Computer wins this round!")
        computer_score += 1
            
play_again = input("Play again? (y/n): ").lower()
if play_again != 'y':
        print("Thanks for playing!")

        break
if __name__ == "__main__":
          play_game()