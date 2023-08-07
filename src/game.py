

def game_intro():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious place...")
    print("Make choices to navigate through different scenarios.\n")

def scenario_1():
    print("Scenario 1: You see a fork in the road.")
    print("Do you go left or right?")
    choice = input("Enter 'left' or 'right': ")
    
    if choice == 'left':
        print("You chose left. You discover a hidden cave.")
        scenario_2()
    elif choice == 'right':
        print("You chose right. You encounter a wild animal.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        scenario_1()

def scenario_2():
    print("\nScenario 2: Inside the cave, you find a treasure chest.")
    print("Do you open it or leave it?")
    choice = input("Enter 'open' or 'leave': ")
    
    if choice == 'open':
        print("You opened the chest and found a valuable gem!")
        game_win()
    elif choice == 'leave':
        print("You decide to leave the chest untouched.")
        print("As you exit the cave, you see a path leading deeper into the forest.")
        scenario_3()
    else:
        print("Invalid choice. Try again.")
        scenario_2()

def scenario_3():
    print("\nScenario 3: You follow the path and come across a river.")
    print("Do you try to swim across or search for a bridge?")
    choice = input("Enter 'swim' or 'bridge': ")
    
    if choice == 'swim':
        print("You attempt to swim across but get caught in a strong current.")
        game_over()
    elif choice == 'bridge':
        print("You find a sturdy bridge and cross the river safely.")
        print("You emerge on the other side of the river and spot a village in the distance.")
        print("Congratulations! You successfully navigated the challenges and reached the village.")
        game_win()
    else:
        print("Invalid choice. Try again.")
        scenario_3()

def game_over():
    print("\nGame Over! You lost.")
    play_again()

def game_win():
    print("\nCongratulations! You won.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == 'yes':
        start_game()
    else:
        print("Thank you for playing!")

def start_game():
    game_intro()
    scenario_1()

if __name__ == "__main__":
    start_game()