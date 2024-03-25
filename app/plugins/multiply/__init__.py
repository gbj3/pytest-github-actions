from app.commands import Command
from decimal import Decimal
import logging

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

class MultiplyCommand(Command):
        def execute(self):
            multiplicand = input('Enter values to be multiplied: ').split()
            for i in range(0, len(multiplicand)):
                multiplicand[i] = int(multiplicand[i])
            logging.info('Multiplicands {multiplicand[0]} and {multiplicand[1]} were mutiplied to a product of ' + str(multiply(multiplicand[0], multiplicand[1])))
            
            
            print(multiply(multiplicand[0], multiplicand[1]))