import data
import helpers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from UrbanRoutesPage import UrbanRoutesPage
import time


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    #Test 1
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(3)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        time.sleep(2)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #Test 2
    def test_taxi_request(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(1)
        routes_page.click_taxi_request_button()
        time.sleep(1)
        assert True, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'np-button'))

    #Test 3
    def test_select_comfort_category(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_category()
        assert True, expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]'))

    #Test 4
    def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number

        routes_page.click_phone_field()
        time.sleep(1)
        routes_page.set_phone_number(phone_number)
        time.sleep(1)
        routes_page.click_continue_button()
        time.sleep(1)

        code = helpers.retrieve_phone_code(driver=self.driver)
        time.sleep(1)
        routes_page.add_phone_code(code)
        time.sleep(1)
        routes_page.click_confirm_button()
        time.sleep(1)
        assert routes_page.get_phone() == phone_number


    #Test 5
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(1)
        card_number = data.card_number
        time.sleep(1)
        card_code = data.card_code
        time.sleep(1)
        routes_page.set_steps_payment_method(card_number, card_code)
        time.sleep(1)
        assert True, routes_page.check_agree_card()
        time.sleep(1)
        routes_page.click_close_pop_up_card_windows()
        time.sleep(1)

    #Test 6
    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    #Test 7
    def test_blanket_is_selected(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_selector()
        time.sleep(3)
        assert routes_page.get_blanket_value() == 'on'

    #Test 8
    def test_add_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        for _ in range(2):
            routes_page.click_ice_cream_plus()
            time.sleep(1)
        assert routes_page.get_ice_cream_value() == '2'

    #Test 9
    def test_taxi_request_modal_display(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_find_taxi()
        time.sleep(3)
        assert True, routes_page.check_header_order_title()

        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(20)
        assert True, routes_page.check_taxi_driver_is_selected()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
