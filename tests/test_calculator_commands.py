# test_calculator_commands.py
import os  
import re
import pytest
from unittest.mock import patch
from main import main

base_dir = os.path.dirname(os.path.dirname(__file__))
plugins_path = os.path.join(base_dir, 'calculator', 'plugins')

@pytest.mark.parametrize("command, inputs, expected_output_pattern", [
    # Test cases...
])
def test_calculator_operations(command, inputs, expected_output_pattern, monkeypatch):
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    with patch('builtins.print') as mock_print:
        try:
            main(plugins_path=plugins_path)  # Pass plugins_path to main
        except SystemExit:
            pass

        printed_output = " ".join(str(call.args[0]) for call in mock_print.call_args_list)
        match = re.search(expected_output_pattern, printed_output)
        assert match is not None, f"Expected pattern '{expected_output_pattern}' not found in printed output."
