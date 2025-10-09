# …/m_softdev/tests/test_debug_var.py


from m_softdev.debug import debug_var


def test_debug_var(capsys):
    var = "bla"
    debug_var("var", var)
    captured = capsys.readouterr()
    assert "bla" in captured.out

