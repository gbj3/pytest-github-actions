'''test_commands.py'''

import pytest
from app import App
# from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
        
def test_add_command(capfd, monkeypatch):
    """Test the execution of the AddCommand."""
    inputs = iter(['5 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = AddCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "12"

    
def test_subtract_command(capfd, monkeypatch):
    """Test the execution of the SubtractCommand."""
    inputs = iter(['7 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = SubtractCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "0"

    
def test_multiply_command(capfd, monkeypatch):
    """Test the execution of the MultiplyCommand."""
    inputs = iter(['5 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = MultiplyCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "35"
    
def test_divide_command(capfd, monkeypatch):
    """Test the execution of the DivideCommand."""
    inputs = iter(['7 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = DivideCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "1.0"
