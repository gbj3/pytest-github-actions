from app.commands import Command
from decimal import Decimal
import logging

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        return ValueError("Cannot divide by zero")
    return a / b

class DivideCommand(Command):
    def execute(self):
        try:
            dividends = input('Enter values to be divided: ').split()
            for i in range(0, len(dividends)):
                dividends[i] = int(dividends[i])
            
            logging.info(f'Dividends {dividends[0]} and {dividends[1]} were divided to a quotient of ' + str(divide(dividends[0], dividends[1])))
            print(divide(dividends[0], dividends[1]))

            file = open("./data/operation_history.csv", "a")
            file.write(f"divide,{dividends[0]},{dividends[1]}\n")
            file.close()
        except:
            print(f"Error dividing")
            logging.info(f"Could not divide")