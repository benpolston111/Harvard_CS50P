from bank import value

def test_themoney():
    assert value("hello") == 0
    assert value("help") == 20
    assert value("testing") == 100
    assert value("HELLO") == 0
