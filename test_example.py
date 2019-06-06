import pytest

def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2

#make sure to start function name with test
def test_sum():
    assert sum(1, 2) == 3 
