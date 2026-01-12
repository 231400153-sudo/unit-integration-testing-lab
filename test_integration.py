from bank_app import transfer, deposit, calculate_interest
import pytest

def test_transfer_success():
    balance_from = 1000
    balance_to = 500
    amount = 200
    new_balance_from, new_balance_to = transfer(balance_from, balance_to, amount)
    assert new_balance_from == 800
    assert new_balance_to == 700

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(100, 500, 200)  # cannot transfer more than balance

def test_transfer_and_interest():
    balance_from = 1000
    balance_to = 500
    amount = 200
    # transfer first
    new_balance_from, new_balance_to = transfer(balance_from, balance_to, amount)
    # then calculate interest on receiver
    new_balance_to_interest = calculate_interest(new_balance_to, 5, 1)
    assert new_balance_to_interest == new_balance_to * 1.05
