from app.commands import Command
from decimal import Decimal

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        return ValueError("Cannot divide by zero")
    return a / b

class DivideCommand(Command):
    def execute(self):
        dividends = input('Enter values to be divided: ').split()
        for i in range(0, len(dividends)):
            dividends[i] = int(dividends[i])
        
        print(divide(dividends[0], dividends[1]))