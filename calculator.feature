Feature: Calculator
    Develop a Calculator

    Scenario: “+” should add to current total
        Given the current total is “5”
        When I enter “7”
        Then the current total should be “12”