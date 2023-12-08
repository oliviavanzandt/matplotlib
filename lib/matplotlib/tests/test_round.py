

import pytest  # Assuming you're using pytest for testing


def test_round_function():
    dpi = 100
    h = 1708
    height_inches = float(h) / dpi * dpi

    # Check that the original value is not rounded
    assert height_inches == 1707.9999999999998

    # Round and assign value back to the variable
    height_inches = round(height_inches)

    # Check that the rounded value is equal to the expected value
    assert height_inches == 1708

# Run the tests when the script is executed
if __name__ == "__main__":
    pytest.main([__file__])
