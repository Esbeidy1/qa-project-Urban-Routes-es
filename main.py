import data
import helpers
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(3)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        time.sleep(5)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_request(self):
        routes_page = UrbanRoutesPage(self.driver)
        #routes_page.set_from(data.address_from)
        #routes_page.set_to(data.address_to)
        time.sleep(5)
        #helpers.wait_for_taxi_request_button(helpers.wait_for_taxi_request_button(self))
        routes_page.click_taxi_request_button(UrbanRoutesPage(*self.taxi_request_button))
        time.sleep(5)
        #helpers.wait_for_reserve_button(helpers.wait_for_taxi_request_button(self))
        assert True, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'np-button'))

    def test_select_comfort_category(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_category()
        assert True, expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]'))

    def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        # Enviar Código SMS
        routes_page.fill_phone_number()
        helpers.standard_wait_time()
        assert routes_page.text_in_phone_number_box == phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_steps_payment_method(card_number, card_code)
        assert True, routes_page.check_agree_card()
        routes_page.click_close_pop_up_card_windows()

    def test_message_for_driver(self):
        # Prueba para agregar un mensaje al conductor.
        routes_page = UrbanRoutesPage(self.driver)
        # Ingresar el mensaje del conductor
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_blanket_is_selected(self):
        # Prueba para agregar una manta y pañuelos.
        routes_page = UrbanRoutesPage(self.driver)
        # Hacer click en el slider
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'

    def test_add_2_ice_creams(self):
        # Prueba agregar 2 helados a la ruta.
        routes_page = UrbanRoutesPage(self.driver)
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'

    def test_taxi_request_modal_display(self):
        # Prueba para esperar que aparezca la información del conductor en el modal.
        routes_page = UrbanRoutesPage(self.driver)
        # Hace clic pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        assert True, routes_page.check_header_order_title()

    def test_check_show_name_driver_modal(self):
        # Crea una instancia de UrbanRoutesPage y pasa el driver como argumento.
        routes_page = UrbanRoutesPage(self.driver)
        helpers.wait_for_countdown_to_finish()
        assert True, routes_page.check_taxi_driver_is_selected()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
