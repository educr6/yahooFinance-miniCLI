import pytest

def func(x):
    return x + 1

def test_ThreePlusOneEquals4():
    assert func(3) == 4

def test_FourPlusOneEquals5():
    assert func(4) == 5
