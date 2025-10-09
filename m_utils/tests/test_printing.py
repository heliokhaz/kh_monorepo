# …/m_utils/tests/test_printing.py


from m_utils.printing import fancy_print

def test_fancy_print(capsys):
    fancy_print("hello")
    captured = capsys.readouterr()
    assert "hello" in captured.out
