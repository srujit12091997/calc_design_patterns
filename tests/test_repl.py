# test_repl.py
import os
import pytest
from unittest.mock import patch, MagicMock  # Import MagicMock
from main import main

base_dir = os.path.dirname(os.path.dirname(__file__))
plugins_path = os.path.join(base_dir, 'calculator', 'plugins')

@pytest.fixture
def mock_inputs(monkeypatch):
    mock_input = MagicMock()
    mock_print = MagicMock()
    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)
    return mock_input, mock_print


def test_repl_exit_command(mock_inputs):
    mock_input, mock_print = mock_inputs
    mock_input.side_effect = ['exit']

    with pytest.raises(SystemExit):
        main(plugins_path=plugins_path)
    
    mock_print.assert_called_with("Exiting the application.")

def test_repl_unknown_command(mock_inputs):
    mock_input, mock_print = mock_inputs
    mock_input.side_effect = ['unknown_command', 'exit']

    with pytest.raises(SystemExit):
        main(plugins_path=plugins_path)

    # Check that the specific message was printed
    mock_print.assert_any_call("Unknown command. Please type 'menu' to see available commands.")


def test_repl_menu_command(mock_inputs):
    mock_input, mock_print = mock_inputs
    mock_input.side_effect = ['menu', 'exit']

    with pytest.raises(SystemExit):
        main(plugins_path=plugins_path)
    
    mock_print.assert_any_call('Available commands:')
