Feature: User Management API Automation
  As a developer, I want to ensure the users API endpoints function correctly

  Scenario: Fetch an existing user details
    Given the user endpoint "/users/1" is available
    When I send a GET request to fetch the user
    Then the response status code should be 200
    And the response should contain the user name "Leanne Graham"

  Scenario Outline: Create a new user dynamically
    Given the user endpoint "/users" is available
    When I send a POST request with name "<name>", username "<username>", and email "<email>"
    Then the response status code should be 201
    And the response should contain the user name "<name>"

    Examples:
      | name          | username | email               |
      | Arpan Pal     | arpanpal   | arpanpalbwn@gmail.com   |
      | random        | random   | random              |
