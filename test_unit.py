from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility
import pytest

def test_deposit_valid():
    assert deposit(1000, 500) == 1500  # valid deposit

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)  # invalid deposit, must give balance and amount

def test_withdraw_valid():
    assert withdraw(1000, 500) == 500

def test_withdraw_invalid_negative():
    with pytest.raises(ValueError):
        withdraw(1000, -50)

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(500, 600)

def test_calculate_interest_valid():
    assert calculate_interest(1000, 5, 2) == 1000 * (1 + 5/100) ** 2

def test_calculate_interest_invalid_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_check_loan_eligibility_true():
    assert check_loan_eligibility(6000, 750) == True

def test_check_loan_eligibility_false():
    assert check_loan_eligibility(4000, 650) == False
