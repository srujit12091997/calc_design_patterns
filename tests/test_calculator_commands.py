import re
import pytest
from unittest.mock import patch
from main import main

@pytest.mark.parametrize("command, inputs, expected_output_pattern", [
    ('add', ['add', '1 2 3 4', 'exit'], r"The result of add is: 10"),
    ('subtract', ['subtract', '10 2', 'exit'], r"The result of subtract is: 8"),
    ('multiply', ['multiply', '2 3 4', 'exit'], r"The result of multiply is: 24"),
    ('divide', ['divide', '20 2', 'exit'], r"The result of divide is: 10"),
    ('divide', ['divide', '20 0', 'exit'], r"Error: Cannot divide by zero"),
])
def test_calculator_operations(command, inputs, expected_output_pattern, monkeypatch):
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    with patch('builtins.print') as mock_print:
        try:
            main()
        except SystemExit:
            pass  # Handle the SystemExit exception to continue execution

        printed_output = " ".join(str(call.args[0]) for call in mock_print.call_args_list)
        print("Debug - Printed Output:", printed_output)  # Debug print
        
        # Use regex to search for the expected pattern in the printed output
        match = re.search(expected_output_pattern, printed_output)
        assert match is not None, f"Expected pattern '{expected_output_pattern}' not found in printed output."
