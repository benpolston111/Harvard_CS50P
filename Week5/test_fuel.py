from fuel import convert,gauge
import pytest

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(0) == "E"

def test_convert():
    assert convert("10/10") == 100
    assert convert("1/100") == 1
    assert convert("1/1000") == 0
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("7/0")
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("bat/cat")
