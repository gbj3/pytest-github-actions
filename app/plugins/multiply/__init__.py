from app.commands import Command
from decimal import Decimal
import logging

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

class MultiplyCommand(Command):
        def execute(self):
            try:
                multiplicand = input('Enter values to be multiplied: ').split()
                for i in range(0, len(multiplicand)):
                    multiplicand[i] = int(multiplicand[i])

                logging.info(f'Multiplicands {multiplicand[0]} and {multiplicand[1]} were mutiplied to a product of ' + str(multiply(multiplicand[0], multiplicand[1])))

                file = open("./data/operation_history.csv", "a")
                file.write(f"multiply,{multiplicand[0]},{multiplicand[1]}\n")
                file.close()      
                
                print(multiply(multiplicand[0], multiplicand[1]))
            except:
                 print(f"Unable to multiply")
                 logging.info(f"Unable to use multiply command")