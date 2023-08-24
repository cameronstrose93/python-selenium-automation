
Feature: Test for Search items and Cart

  Scenario: Search for item, place in cart, and verify item is in cart
    Given Open Amazon page
    When Search For cat
    Then Click on Product
    Then Add Product to Cart
    Then Click No Coverage
    When Click on cart icon
    Then Verify that 1 item is in the Cart
    Then Verify that item is in the cart