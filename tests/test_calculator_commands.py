# test_calculator_commands.py
import pytest
from unittest.mock import patch
from main import main

@pytest.mark.parametrize("command, inputs, expected_output", [
    ('add', ['add', '1 2 3 4', 'exit'], "The result of add is: 10"),
    ('subtract', ['subtract', '10 2', 'exit'], "The result of subtract is: 8"),
    ('multiply', ['multiply', '2 3 4', 'exit'], "The result of multiply is: 24"),
    ('divide', ['divide', '20 2', 'exit'], "The result of divide is: 10"),
    ('divide', ['divide', '20 0', 'exit'], "Error: Cannot divide by zero"),
])
def test_calculator_operations(command, inputs, expected_output, monkeypatch):
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda *args: next(inputs_iter))
    with patch('builtins.print') as mock_print:
        with pytest.raises(SystemExit):
            main()

        # Debug: Print all captured outputs
        all_printed_output = [call.args[0] for call in mock_print.call_args_list]
        print("All printed output:", all_printed_output)

        # Attempt to find the expected output in all printed output
        found = any(expected_output in call for call in all_printed_output)
        assert found, f"Expected output '{expected_output}' not found in printed output."