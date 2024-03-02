# test_repl.py
import pytest
from unittest.mock import patch
from main import main

def test_repl_exit_command(monkeypatch):
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    with patch('builtins.print') as mock_print:
        with pytest.raises(SystemExit):
            main()
        mock_print.assert_any_call("Type 'menu' for commands or 'exit' to quit: ")

def test_repl_unknown_command(monkeypatch):
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    with patch('builtins.print') as mock_print:
        with pytest.raises(SystemExit):
            main()
        mock_print.assert_any_call("Unknown command. Please type 'menu' to see available commands.")

def test_repl_menu_command(monkeypatch):
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    with patch('builtins.print') as mock_print:
        with pytest.raises(SystemExit):
            main()
        mock_print.assert_any_call('Available commands:')
