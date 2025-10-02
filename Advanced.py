import random
import os

# Mapping
yourDict = {"R": 1, "P": 2, "S": 3}
reverse = {1: "Rock", 2: "Paper", 3: "Scissors"}

# Score variables
your_score = 0
comp_score = 0
draws = 0
rounds = 0

def clear_screen():
    # Clear screen for better UX (works on Windows/Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print("🎮 Rock Paper Scissors Game")
    print("----------------------------")
    print("Choose: [R]ock, [P]aper, [S]cissors or 1/2/3")
    print(f"📊 Score - You: {your_score} | Computer: {comp_score} | Draws: {draws} | Rounds: {rounds}")
    print("----------------------------")

    # Input
    your = input("👉 Your choice: ").strip().upper()

    # Validate and convert input
    if your.isdigit() and int(your) in [1, 2, 3]:
        you = int(your)
    elif your in yourDict:
        you = yourDict[your]
    else:
        print("❌ Invalid input! Try R/P/S or 1/2/3.")
        input("Press Enter to try again...")
        continue

    # Computer choice
    computer = random.choice([1, 2, 3])

    # Show choices
    print(f"\n🧠 Computer chose: {reverse[computer]}")
    print(f"🧍 You chose: {reverse[you]}\n")

    # Game logic
    if computer == you:
        print("🤝 It's a Draw!")
        draws += 1
    elif (computer == 1 and you == 2) or \
         (computer == 2 and you == 3) or \
         (computer == 3 and you == 1):
        print("✅ You Win this round!")
        your_score += 1
    else:
        print("❌ You Lose this round!")
        comp_score += 1

    rounds += 1

    # Ask to play again
    again = input("\n🔁 Play again? (Y/N): ").strip().lower()
    if again not in ['y', 'yes']:
        clear_screen()
        print("🏁 Game Over")
        print("----------------------------")
        print(f"🧍 You: {your_score} wins")
        print(f"🧠 Computer: {comp_score} wins")
        print(f"🤝 Draws: {draws}")
        print(f"🎯 Total Rounds Played: {rounds}")
        print("-----------------------------")
        break
