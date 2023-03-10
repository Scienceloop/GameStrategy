import random

# Define the wheel pockets and their corresponding colors
pockets = {
        0: "green",
        37: "green",
        1: "red",
        2: "black",
        3: "red",
        4: "black",
        5: "red",
        6: "black",
        7: "red",
        8: "black",
        9: "red",
        10: "black",
        11: "black",
        12: "red",
        13: "black",
        14: "red",
        15: "black",
        16: "red",
        17: "black",
        18: "red",
        19: "red",
        20: "black",
        21: "red",
        22: "black",
        23: "red",
        24: "black",
        25: "red",
        26: "black",
        27: "red",
        28: "black",
        29: "black",
        30: "red",
        31: "black",
        32: "red",
        33: "black",
        34: "red",
        35: "black",
        36: "red"
    }

def roulette(bet, color):

    house_edge = 1 - 0.02

    # Define a function to spin the wheel and return the winning number
    def spin_wheel():
        return random.choice(list(pockets.keys()))

        # Define a function to place a bet and return the payout amount

    def place_bet(bet, color, number):
        if bet > 0 and color in pockets.values() and number in pockets:
            if pockets[number] == color:
                if pockets[number] == "green":
                    return bet * 17 * house_edge
                else:
                    return bet * 2 * house_edge
            else:
                return -bet
        else:
            return 0

    # Play the game
    number = spin_wheel()
    payout = place_bet(bet, color, number)
    if payout > 0:
        return payout
    elif payout == 0:
        return None
    else:
        return payout
