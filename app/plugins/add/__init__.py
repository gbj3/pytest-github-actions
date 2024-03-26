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
        try:
            addend = input('Enter values to be added: ').split()
            for i in range(0, len(addend)):
                addend[i] = int(addend[i])
            logging.info(f"Addends {addend[0]} and {addend[1]} were added to a sum of " + str(add(addend[0], addend[1])))

            file = open("./data/operation_history.csv", "a")
            file.write(f"add,{addend[0]},{addend[1]}\n")
            file.close()
        
            print(add(addend[0], addend[1]))
        except:
            print(f"Error adding")
            logging.info("Adding command error")
