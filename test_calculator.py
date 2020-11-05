from pytest_bdd import scenario, given, when, then

cur_total = 0
entered_val = 0

@scenario('calculator.feature','“+” should add to current total')
def test_publish():
    pass

@given('the current total is “5”')
def current_total():
    global cur_total
    cur_total = 5

@when('I enter “7”')
def enter_val():
    global entered_val
    entered_val = 7

@then('the current total should be “12”')
def calc_cur_total():
    global cur_total
    cur_total = cur_total + entered_val

    assert cur_total == 12, "Total should be equal to 12, but its not!"