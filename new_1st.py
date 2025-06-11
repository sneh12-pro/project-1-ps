import random




# Dictionaries for conversion
yourDict = {"R": 1, "P": 2, "S": 3}
reverse = {1: "Rock", 2: "Paper", 3: "Scissors"}

while True:
    computer = random.choice([1, 2, 3])
# Input from user
    your = input("Enter your choice (R/P/S or 1/2/3): ").strip().upper()

    # Convert input to number
    if your.isdigit() and int(your) in [1, 2, 3]:
        you = int(your)
    elif your in yourDict:
        you = yourDict[your]
    else:
        print("❌ Invalid input. Please enter R, P, S or 1, 2, 3.")
        exit()

    # Show choices
    print(f"Computer's choice is {reverse[computer]} \nYour choice is {reverse[you]}")

    # Game logic
    if computer == you:
        print("It's a Draw!")
    elif (computer == 1 and you == 2) or \
        (computer == 2 and you == 3) or \
        (computer == 3 and you == 1):
        print("✅ You win!")
    else:
        print("❌ You lose!")

    Play_again = input("do you wanna play again? \n(yes/no) ")
    if(Play_again not in ["yes" ,"y" ]):
        print("thanks for playing")
        break
