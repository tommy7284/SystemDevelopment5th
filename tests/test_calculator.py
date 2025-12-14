"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        calc = Calculator()
        # -5 - (-3) = -2
        assert calc.subtract(-5, -3) == -2

    def test_subtract_result_zero(self):
        """Test subtraction that results in zero."""
        calc = Calculator()
        # 5 - 5 = 0
        assert calc.subtract(5, 5) == 0


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 4
        b = 3
        expected = 12

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
        
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        calc = Calculator()
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 5) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        calc = Calculator()
        assert calc.multiply(4, -3) == -12
        assert calc.multiply(-4, -3) == 12


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises standard ZeroDivisionError."""
        # Note: Depending on implementation, this might raise ValueError or ZeroDivisionError
        calc = Calculator()
        with pytest.raises(ValueError):
             calc.divide(10, 0)
            
    def test_divide_result_float(self):
        """Test division resulting in float."""
        calc = Calculator()
        assert calc.divide(5, 2) == 2.5

class TestExceptions:
    """Tests for invalid input exceptions based on Slide 35."""
    def test_add_max_value(self):
        """境界値 (1,000,000) が正常に処理されるかテスト"""
        calc = Calculator()
        assert calc.add(1000000, 0) == 1000000

    def test_add_min_value(self):
        """境界値 (-1,000,000) が正常に処理されるかテスト"""
        calc = Calculator()
        assert calc.add(-1000000, 0) == -1000000
        
    def test_input_too_large(self):
        """Test that input larger than MAX_VALUE raises InvalidInputException."""
        calc = Calculator()
        # 1,000,000 is valid, 1,000,001 should fail
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 1)

    def test_input_too_small(self):
        """Test that input smaller than MIN_VALUE raises InvalidInputException."""
        calc = Calculator()
        # -1,000,000 is valid, -1,000,001 should fail
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 1)
            
    def test_subtract_input_too_large(self):
        """Test subtraction with invalid input."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1000001, 1)

    def test_multiply_input_too_large(self):
        """Test multiplication with invalid input."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1000001, 1)

    def test_divide_input_too_large(self):
        """Test division with invalid input."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1000001, 1)

    def test_add_input_too_large_second_arg(self):
        """Test adding when second argument is too large."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1, 1000001)

    def test_subtract_input_too_large_second_arg(self):
        """Test subtraction when second argument is too large."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1, 1000001)

    def test_multiply_input_too_large_second_arg(self):
        """Test multiplication when second argument is too large."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000001)

    def test_divide_input_too_large_second_arg(self):
        """Test division when second argument is too large."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000001)
            
    def test_exception_message(self):
        """Test that the exception message contains correct values."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(1000001, 0)
        assert "1000001" in str(exc_info.value)