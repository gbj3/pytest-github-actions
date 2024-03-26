from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f"Greet, Add, Subtract, Multiply, Divide, Csv, Data, Exit")