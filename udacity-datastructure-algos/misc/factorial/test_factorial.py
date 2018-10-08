import factorial
import pytest

@pytest.mark.parametrize("test_input, test_output",
[
    (4, 24),
    (10, 3628800),
    (5, 120),
    (7, 5040),
    (0, 1)

])
def test_factorial(test_input, test_output):
    result = factorial.factorial_calc(test_input) 
    
    assert result == test_output

