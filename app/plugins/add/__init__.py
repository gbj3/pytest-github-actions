from app.commands import Command
# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable
# Import arithmetic operations from a module named calculator.operations
import logging

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

class AddCommand(Command):
    def execute(self):
        addends = input('Enter values to be added: ').split()
        for i in range(0, len(addends)):
            addends[i] = int(addends[i])
        logging.info('Addends {addends[0]} and {addends[1]} were added to a sum of ' + str(add(addends[0], addends[1])))
        
        print(add(addends[0], addends[1]))