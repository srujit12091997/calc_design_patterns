# conftest.py
import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

@pytest.fixture
def num_records(request):
    """Fixture to access the number of records specified by the command-line option."""
    return request.config.getoption("--num_records")

def test_data_generator(number_of_tests):
    """Generates test data for calculator operations."""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(number_of_tests):
        num_a = Decimal(fake.random_number(digits=2))
        num_b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_key = fake.random_element(elements=list(operations.keys()))
        operation = operations[operation_key]

        if operation == divide and num_b == 0:
            num_b = Decimal('1')  # Adjust to avoid division by zero

        expected_result = calculate_expected_result(operation, num_a, num_b)

        yield num_a, num_b, operation_key, operation, expected_result

def calculate_expected_result(operation, num_a, num_b):
    """Calculates the expected result or catches a ZeroDivisionError."""
    try:
        return operation(num_a, num_b)
    except ZeroDivisionError:
        return "ZeroDivisionError"

def pytest_generate_tests(metafunc):
    """Generates tests based on the number of records specified by the --num_records option."""
    if 'num_records' in metafunc.fixturenames:
        num_records = metafunc.config.getoption("--num_records")
        test_cases = list(test_data_generator(num_records))
        adapted_cases = [
            (a, b, operation_key if 'operation_name' in metafunc.fixturenames else operation, expected)
            for a, b, operation_key, operation, expected in test_cases
        ]
        metafunc.parametrize("a,b,operation,expected", adapted_cases)
