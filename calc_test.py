"""
Unit tests for the calculator library
"""

import calc


class TestCalculator:

    def test_subtraction(self):
        assert 2 == calc.sub(4, 2)

    def test_addition(self):
        assert 4 == calc.add(2, 2)

    def test_mul(self):
        assert 6 == calc.mul(3, 2)

    def test_dev(self):
        assert 15 == calc.dev(150/10)