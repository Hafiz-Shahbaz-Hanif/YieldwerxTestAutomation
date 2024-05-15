Feature: Login Functionality

  @login
  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid username and valid password into the fields
        |username  |password  |
        |michael   |Test.123  |
    And I click on Login button
    Then I should get logged in


