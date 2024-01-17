from twttr import shorten

def test_twit():
    assert shorten("test") == "tst"
    assert shorten("tEst") == "tst"
    assert shorten("t3st") == "t3st"
    assert shorten("t@st") == "t@st"
    assert shorten(".,!@?") == ".,!@?"
