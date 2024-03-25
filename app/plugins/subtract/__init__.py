from app.commands import Command
from decimal import Decimal
import logging

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

class SubtractCommand(Command):
    def execute(self):
        subtractant = input('Enter values to be subtracted: ').split()
        for i in range(0, len(subtractant)):
            subtractant[i] = int(subtractant[i])

        logging.info('Subtractants {subtractant[0]} and {subtractant[1]} were subtracted to a difference of ' + str(subtract(subtractant[0], subtractant[1])))
        
        print(subtract(subtractant[0], subtractant[1]))