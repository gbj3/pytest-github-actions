from app.commands import Command
from decimal import Decimal

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

class MultiplyCommand(Command):
        def execute(self):
            multiplicand = input('Enter values to be multiplied: ').split()
            for i in range(0, len(multiplicand)):
                multiplicand[i] = int(multiplicand[i])
            
            print(multiply(multiplicand[0], multiplicand[1]))