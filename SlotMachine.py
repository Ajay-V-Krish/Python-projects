import random

print('')
print('-------------------------Slot Machine------------------------------')
print('')
print('''
      Rules:
        1)The Slot Machine contains 3 rows and 3 columns.
        2)If you get same symbols on each row you will get double f the amount you bet on each row.
        3)Before entering you have to deposit somr amount.
        4)You have to choose the no of lines to bet on and the amount you bet on each line.
        5)You can play only until you have balance.''')

MAX_LINES = 3
MAX_BET_AMOUNT = 100
MIN_BET_AMOUNT = 1

ROWS = 3
COLS = 3

symbol_count = {
    "⨁":2,
    "⨇":4,
    "⨎":6,
    "⨅":8
}

symbol_value = {
    "⨁":5,
    "⨇":4,
    "⨎":3,
    "⨅":2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)
    
    return winnings, winning_line

def slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.append(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
    
        print()
       

def main_deposit():
    while True:
        deposit = input("How much amount would you like to deposit? $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print('')
                print("Deposit must be greater than 0")
                print('')
        else:
            print('')
            print("Please enter a number.")
            print('')
            
    return deposit

def slot_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + '):')
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('')
                print("Enter valid number of lines.")
                print('')
        else:
            print('')
            print("Please enter a number.")
            print('')
            
    return lines

def bet_amount():
    while True:
        amount = input('Enter the amount to bet on each line($1-$100): $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET_AMOUNT <= amount <= MAX_BET_AMOUNT :
                break
            else:
                print('')
                print("Enter valid amount.")
                print('')
        else:
            print('')
            print("Please enter a number.")
            print('')
            
    return amount

def spin(balance):
        lines = slot_lines()
        while True:
            amount = bet_amount()
            total_amount = amount*lines
            if total_amount > balance:
                print('')
                print(f"You don't have enough balance to bet that amount. Your balance is {balance}") 
                print('')
            else:
                break
        print('')
        print(f"You are betting ${amount} on {lines} lines. Total bet amount is: ${total_amount}")
        print('')
        
        slot_machine = slot_machine_spin(ROWS,COLS,symbol_count)
        print_slot_machine(slot_machine)
        
        winnings,winning_lines = check_win(slot_machine, lines, amount, symbol_value)
        print('')
        print(f"You won ${winnings}.")
        print('')
        print(f"You won on lines: ", *winning_lines)
        print('')
        
        return winnings - total_amount
        
def main():
    balance = main_deposit()
    while True:
        print(f"Current balance is ${balance}")
        print('')
        answer = input("Press enter to spin (q to quit).")
        print('')
        if answer.lower() == 'q':
            break
        balance += spin(balance)
        
    print('')    
    print(f"You are left with ${balance}")
    print('')

main()