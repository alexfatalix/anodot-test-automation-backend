import pytest
from pytemp import pytemp

def test_valid_K2F():
    assert pytemp(40,'kelvin', 'fahrenheit') == -387.66999999999996