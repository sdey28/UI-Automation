Feature: Product search on Target

  Scenario: User searches for an item
    Given Go to Target homepage
    When the user enters laptop in the search bar
    And clicks the search button
    Then verify search results for "laptop" displayed

