from app.commands import Command
from decimal import Decimal
import logging

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        return ValueError("Cannot divide by zero")
    return a / b

class DivideCommand(Command):
    def execute(self):
        dividends = input('Enter values to be divided: ').split()
        for i in range(0, len(dividends)):
            dividends[i] = int(dividends[i])
        logging.info('Dividends {dividends[0]} and {dividends[1]} were divided to a quotient of ' + str(divide(dividends[0], dividends[1])))
        
        print(divide(dividends[0], dividends[1]))