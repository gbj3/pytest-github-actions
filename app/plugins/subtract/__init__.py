from app.commands import Command
from decimal import Decimal

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

class SubtractCommand(Command):
    def execute(self):
        subtractant = input('Enter values to be subtracted: ').split()
        for i in range(0, len(subtractant)):
            subtractant[i] = int(subtractant[i])
        
        print(subtract(subtractant[0], subtractant[1]))