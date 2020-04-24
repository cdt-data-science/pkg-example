from pkg_example.calculator_module import Calculator

def test_double():
    calc = Calculator()
    assert calc.double(3) == 6
    assert calc.double(3.0) == 6.0
