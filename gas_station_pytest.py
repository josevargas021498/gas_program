def test_pay():
    assert gas_core1.pay(10, 1.89) == 18.9
    assert gas_core1.pay(10, 1.99) == 19.9
    assert gas_core1.pay(10, 2.09) == 20.9