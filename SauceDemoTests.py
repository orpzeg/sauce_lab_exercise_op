import argparse
import sys
import unittest

from testlibraries.webdriverfactory import WebDriverFactory
from pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.InventoryDetailPage import InventoryDetailPage
from pages.SauceDemoLoginPage import SauceDemoLoginPage


class SauceDemoTests(unittest.TestCase):
    driver = None
    drivername = ''

    def setUp(self):
        self.factory = WebDriverFactory(self.drivername)
        self.driver = self.factory.get_web_driver_instance()
        self.sauceloginpage = SauceDemoLoginPage(self.driver)
        self.sauceloginpage.gotopage()
        self.sauceloginpage.set_credentials("standard_user", "secret_sauce")
        self.inventory = self.sauceloginpage.clicklogin()

    def test_can_i_login(self):
        self.assertEqual(len(self.inventory.get_products()), 6)

    def test_can_i_can_review_by_item(self):
        products_added_count = 1
        # Iterate through each product available.
        for product in self.inventory.get_products():
            # Navigate to the product's detail page.
            product_detail_page: InventoryDetailPage = product.view_detail()

            # Add the current product to the cart.
            product_detail_page.click_add_to_cart()

            # Retrieve the number of products currently in the cart.
            products_in_cart = product_detail_page.get_count_products_incart()

            # Assert that the product price follows the expected format.
            self.assertRegex(product_detail_page.get_price(), ".*\\.99",
                             "Price of the product does end in .99")

            # Assert that the number of products in the cart matches the expected count.
            self.assertEqual(products_in_cart, products_added_count,
                             f"Expected {products_added_count} products in the cart, found {products_in_cart}")

            # Navigate back to the list of products.
            product_detail_page.click_back_to_products()

            # Update the count of products added for the next iteration.
            products_added_count += 1

    def test_i_can_review_cost_all_of_them(self):
        # Initialize total_cost to 0. This will keep track of the cumulative cost of all products.
        total_cost = 0

        # Iterate through all products retrieved from the inventory.
        for product in self.inventory.get_products():
            # Add the cost of the current product to the total_cost.
            total_cost += product.get_cost().amount

            # Click to add the current product to the cart.
            product.click_add_to_cart()

        # Navigate to the cart page.
        cart_page: CartPage = self.inventory.click_cart()

        # From the cart page, initiate the checkout process.
        checkout_step_one_page: CheckoutStepOnePage = cart_page.click_checkout()

        # Fill in the user's information required for checkout.
        checkout_step_one_page.set_my_information("first name", "last name", "zip code")

        # Proceed to the next step of the checkout process.
        checkout_step_two_page: CheckoutStepTwoPage = checkout_step_one_page.click_continue()

        # Assert that the total cost displayed on the checkout page matches the calculated total cost.
        # This verifies that all products have been added to the cart and their total cost is correct.
        self.assertEqual(checkout_step_two_page.get_total_cost().amount, total_cost)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test parser")
    parser.add_argument('--webdriver', default='chrome', help='Favourite driver')
    # Parse known args and leave the rest for unittest
    args, remaining_argv = parser.parse_known_args()
    SauceDemoTests.drivername = args.webdriver

    # Ensure only unittest arguments are passed along
    sys.argv[1:] = remaining_argv

    # Now you can run unittest with its arguments
    unittest.main()
