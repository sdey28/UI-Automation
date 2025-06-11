Feature: Target Login Functionality

  Scenario: Valid user logs into Target.com
    Given Open Target login page
    When Click on account icon
    When click on side nav sign in button
    And user enters valid email
    And user enters valid password
    And clicks the sign in button
   Then the user should be logged in successfully