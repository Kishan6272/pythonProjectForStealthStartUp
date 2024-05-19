# Created by Kishan Kumar Pandey at 5/18/2024
Feature: Search Functionality

  Scenario: Search for a valid product
    Given  I got navigated to home page
    When I enter a valid product in the Search box field
    And  I click on Search button
    Then Valid product should get displayed in the Search results



  Scenario: Search for a invalid product
    Given  I got navigated to home page
    When I enter a invalid product in the Search box field
    And  I click on Search button
    Then inValid product should not get displayed in the Search results

   Scenario: Search without entering any product
    Given  I got navigated to home page
    When I  dont enter anything into the Search box field
    And  I click on Search button
    Then Proper message should  displayed in the Search results

