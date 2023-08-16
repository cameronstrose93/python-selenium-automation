Feature: Verify if Sign In is seen when logged-out users go to Returns & Orders Page. Verify that Amazon Cart is empty when users go to cart.

  Scenario: Logged-out Users go to Returns & orders Page
    Given Open Amazon page
    When Click on Return and Orders icon
    Then Verify Sign in page opened

  Scenario: Users go to Cart Page
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart is empty