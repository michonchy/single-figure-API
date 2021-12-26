import json

import pytest

from single_figure import app

def test_number_check():
    assert app.number_check(1) == "single figure"

def test_number():
    assert app.number("3") == 3 

