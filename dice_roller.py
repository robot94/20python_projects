#Welcome to the dice Roller app
import random



def dice_roll():
    
    DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
    user_input = input("Do you want to rolle the dice Yes/No: ").lower()
    while user_input == "yes":
        
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        
        print(f"Dice rolled: {player1} and {player2}")
        
        print("\n".join(DICE_ART[player1]))
        print("\n".join(DICE_ART[player2]))
        
        
        
        user_input = input("Do you still want to rolle the dice Yes/No: ").lower()

dice_roll()
        