import pytest
from pytemp import pytemp


def test_valid_K2F():
    assert pytemp(40, 'kelvin', 'fahrenheit') == -387.66999999999996

def test_valid_F2K():
    assert pytemp(-387.66999999999996, 'f', 'k') == 40

def test_valid_F2C():
    assert pytemp(200, 'fahrenheit', 'celsius') == 93.33333333333333


def test_valid_C2F():
    assert pytemp(40, 'c', 'f') == 104.0


def test_valid_K2C():
    assert pytemp(40,'k', 'c') == -233.14999999999998


def test_valid_C2K():
    assert pytemp(-233.14999999999998,'celsius','kelvin') == 40


def test_absolute_zero_F2K():
    assert pytemp(-459.67, 'f', 'k') == 0


def test_absolute_zero_K2F():
    assert pytemp(0, 'k', 'f') == -459.66999999999996


def test_below_zero_value_K2F():
    assert pytemp(-10, 'k', 'f') == "Error, value can't be below absolute zero"  # It's a bug


def test_letter_value_C2F():
    try:
        pytemp("wrong", 'c', 'f')
        assert False
    except SystemExit:
        assert True

def test_invalid_from_value():
    try:
        pytemp(40, 'wrong', 'f')
        assert False
    except SystemExit:
        assert True


def test_invalid_to_value():
    try:
        pytemp(40, 'f', 'wrong')
        assert False
    except SystemExit:
        assert True

#TODO add boundary values tests for absolute zero