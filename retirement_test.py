import pytest
from retirement import *

# testing to see if the function can be called
def test_canCall_Retirement_Age_Function():
    calculate_retirement_age(1937)

# test birth year input
@pytest.mark.parametrize("year", [1903, 1922, 1937])
def test_retirementAge_returned_birth_year_1937_orEarlier(year):
    input_year = calculate_retirement_age(year)
    assert input_year == (65, 0)


def test_retirementAge_returned_birth_year_1938():
    input_year = calculate_retirement_age(1938)
    assert input_year == (65, 2)


def test_retirementAge_returned_birth_year_1939():
    input_year = calculate_retirement_age(1938)
    assert input_year == (65, 4)


def test_retirementAge_returned_birth_year_1940():
    input_year = calculate_retirement_age(1940)
    assert input_year == (65, 6)


def test_retirementAge_returned_birth_year_1941():
    input_year = calculate_retirement_age(1941)
    assert input_year == (65, 8)


def test_retirementAge_returned_birth_year_1942():
    input_year = calculate_retirement_age(1942)
    assert input_year == (65, 10)


@pytest.mark.parametrize("year", [1943, 1952, 1954])
def test_retirementAge_returned_birth_year_1943_to_1954(year):
    input_year = calculate_retirement_age(year)
    assert input_year == (66, 0)


def test_retirementAge_returned_birth_year_1955():
    input_year = calculate_retirement_age(1955)
    assert input_year == (66, 2)


def test_retirementAge_returned_birth_year_1956():
    input_year = calculate_retirement_age(1956)
    assert input_year == (66, 4)


def test_retirementAge_returned_birth_year_1957():
    input_year = calculate_retirement_age(1957)
    assert input_year == (66, 6)


def test_retirementAge_returned_birth_year_1958():
    input_year = calculate_retirement_age(1958)
    assert input_year == (66, 8)


def test_retirementAge_returned_birth_year_1959():
    input_year = calculate_retirement_age(1959)
    assert input_year == (66, 10)

# this would fail because you can't have a negative birth year
def test_calculate_retirement_age_when_birth_year_is_negative():
    with pytest.raises(ValueError):
        input_year = calculate_retirement_age(-1999)
        assert input_year == ('Birth year "-1999" must be no earlier than 1900')

# this would fail because you can only go up to 3000
def test_calculate_retirement_age_when_birth_year_is_excessive():
    with pytest.raises(ValueError):
        input_year = calculate_retirement_age(21999)
        assert input_year == ('Birth year "21999" must be earlier than 3000')


# test accuracy of retirement year and month
def test_inputFor_year_month_age_ageInMonths_1938():
    input_year = calculate_retirement_date(1938, 5, 65, 2)
    assert input_year == (2003, 7)


def test_inputFor_year_month_age_ageInMonths_1939():
    input_year = calculate_retirement_date(1939, 12, 65, 4)
    assert input_year == (2005, 4)


def test_inputFor_year_month_age_ageInMonths_1940():
    input_year = calculate_retirement_date(1940, 1, 65, 6)
    assert input_year == (2005, 7)


def test_inputFor_year_month_age_ageInMonths_1941():
    input_year = calculate_retirement_date(1941, 6, 65, 8)
    assert input_year == (2007, 2)


def test_inputFor_year_month_age_ageInMonths_1942():
    input_year = calculate_retirement_date(1942, 6, 65, 10)
    assert input_year == (2008, 4)



def test_inputFor_year_month_age_ageInMonths_1943():
    input_year = calculate_retirement_date(1943, 6, 66, 0)
    assert input_year == (2009, 6)

def test_inputFor_year_month_age_ageInMonths_1954():
    input_year = calculate_retirement_date(1954, 1, 66, 0)
    assert input_year == (2020, 1)

def test_inputFor_year_month_age_ageInMonths_1955():
    input_year = calculate_retirement_date(1955, 8, 66, 2)
    assert input_year == (2021, 10)

def test_inputFor_year_month_age_ageInMonths_1956():
    input_year = calculate_retirement_date(1956, 1, 66, 4)
    assert input_year == (2022, 5)

def test_inputFor_year_month_age_ageInMonths_1957():
    input_year = calculate_retirement_date(1957, 6, 66, 6)
    assert input_year == (2023, 12)

def test_inputFor_year_month_age_ageInMonths_1958():
    input_year = calculate_retirement_date(1958, 9, 66, 8)
    assert input_year == (2025, 5)

def test_inputFor_year_month_age_ageInMonths_1959():
    input_year = calculate_retirement_date(1959, 2, 66, 10)
    assert input_year == (2025, 12)

def test_inputFor_year_month_age_ageInMonths_1960():
    input_year = calculate_retirement_date(1960, 1, 67, 0)
    assert input_year == (2027, 1)

# this would fail because months are only 1 - 12
def test_get_valid_month_number():
    with pytest.raises(ValueError):
        input_year = calculate_retirement_date(1960, 42, 19, 0)
        assert input_year == 'Birth month "42" must be between 1 and 12'


