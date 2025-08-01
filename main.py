import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for col in range(cols):
            column = []
            current_symbol = all_symbols[:]
            for row in range(rows):
                value = random.choice(current_symbol)
                current_symbol.remove(value)
                column.append(value)
            columns.append(column)
    
    return columns
        


def deposit():

    while True:
        amount = input("What is the amount you want to deposit?")

        if amount.isdigit():

            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a number greater than zero")
        else:
            print("Enter a Valid number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Can you please enter the number of lines from 1 - " + str(MAX_LINES) + "? ")
        
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter number between 1 - {MAX_LINES}")
        else:
            print("Enter a number please")
    
    return lines



def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please Enter a number between {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a valid amount")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"The amount stake is greater than the total balance. Your Current Balance is {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines  so your total bet is ${total_bet} ")

main()