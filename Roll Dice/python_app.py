import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "| 1 |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "| 2 |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o3 |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "| 4 |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o5o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o6o|",
            "|o o|",
            "-----",
        ),

    }

    while input("Do you want to roll dice?(Yes/No)").lower() == "yes":
        dice = random.randint(1, 6)
        print("Dice rolled : {}\n{}".format(dice,"\n".join(dice_drawing[dice])))

roll_dice()