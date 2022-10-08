# A slot machine that will take an amount of Balance from user,
# and user will choose number of matches at a time (2 or 3).
# Once the bet amount has been entered, the user will spin the reel and if they win,
# their bet will be multiplied by the number of matches chosen.
# It continues until the user exits or the balance reaches 00.
# Once the user reaches 00, he or she can deposit again.

import random
import sys

Balance = 0


def main():
    print("1. Play 0. Exit")
    inp = input_check([0, 1])
    if inp == 1:
        if Balance == 0:
            Deposit()
        play()
    else:
        sys.exit("Thank you for playing!!")


def Deposit():
    global Balance
    while True:
        try:
            Balance = int(input("Deposit: "))
            if Balance < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Deposit must be greater than 0!!!")
            pass

# Prints the slot machine in a random order
# Return True or False depends on the matches.
def slot_machine(match):
    emoji_list = ["|🍈|", "|🍌|", "|🥭|", "|🍒|", "|🍉|"]

    slot_result_list = [[random.choice(emoji_list) for j in range(3)] for i in range(3)]
    print()
    print("\n\n".join(map(" ".join, slot_result_list)))
    print()

    m_list = [-1, -1, 2, 1]
    for i in range(3):
        if len(set(slot_result_list[i])) == m_list[match]:
            return True
        return False

# Handle any type of mistake or Error while inputting.
def input_check(range):
    while True:
        try:
            inp = int(input("--> "))
            if len(range) == 1 and inp <= range[0]:
                return inp

            elif len(range) == 2 and range[0] <= inp <= range[1]:
                return inp

            elif len(range) == 1 and not inp <= range[0]:
                print("Not Enough Balance!!")
                raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("Choose a Valid Number!!")
            pass

# Main Game
def play():
    global Balance

    # If Balance 0 User get a option for deposit or exit.
    if Balance == 0:
        print("Out of Balance!!\n1. Deposit 0. Exit")
        opt = input_check([0, 1])
        if opt == 1:
            Deposit()
            play()
        else:
            sys.exit(f"Thank you for playing!!")

    print("Enter the num of match (2 or 3): ")
    match = input_check([2, 3])

    print("Enter your bet amount: ")
    bet_amount = input_check([Balance])

    print("1. Spin 0. Exit")
    option = input_check([0, 1])

    if option == 1 and Balance != 0:
        res = slot_machine(match)

        if res:
            # If Won bet get multiplied by the (matches.1) and Add to Balance
            # 1.1 or 2.1 or 3.1
            Balance *= (match + 0.1)
            print("You Won!!")
            print(f"Current Balance: {Balance}$\n")
            main()

        else:
            Balance -= bet_amount
            print("\nBetter Luck Next Time :(")
            print(f"Current Balance: {Balance}$\n")
            main()

    else:
        sys.exit(f"Thank you for playing!!\nCurrent Balance: {Balance}$")


if __name__ == "__main__":
    main()
