from calcdemo import __version__
from calcdemo.calc import Calc
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_add_01():
    assert Calc(9,2).add() == 11


def test_add_02():
    assert Calc(-9, 2).add() == -7

def test_dif_01():
    assert Calc(9, 2).dif() == 7

def test_dif_02():
    assert Calc(-9, 2).dif() == -11

def test_div_01():
    assert Calc(9, 3).div() == 3

def test_div_02():
    with pytest.raises(ZeroDivisionError):
        Calc(9, 0).div()


