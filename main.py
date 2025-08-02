import random
MIN_LINE = 1
MAX_LINE = 3


fruit_order = {

    "🍒" : 2,
    "🍋" : 4,
    "🍇" : 6,
    "🍎" : 8


}

#def get_slot_machine(row, column, fruit_order):


def deposit():
    while True:
        amount = input(f"Enter the amount you want to deposit($) ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Enter a amount greater than zero ")
        else:
            print(f"Enter a valid number ")

    return amount

def number_of_line():
     while True:
        line = input(f"Enter the total line you want to bet on from ({MIN_LINE} - {MAX_LINE}) ")
        if line.isdigit():
            line = int(line)
            if MIN_LINE <= line <= MAX_LINE:
                break
            else:
                print(f"Please enter a value from {MIN_LINE} - {MAX_LINE} ")
        else:
            print(f"Enter a valid number from {MIN_LINE} - {MAX_LINE} ")

     return line


def main():
    balance = deposit()
    line = number_of_line()