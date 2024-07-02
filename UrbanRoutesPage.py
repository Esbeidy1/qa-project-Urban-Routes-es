import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    #Test 1 set_route
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Test 2 taxi_request
    taxi_request_button = (By.XPATH, '// *[ @ id = "root"] / div / div[3] / div[3] / div[1] / div[3] / div[1] / button')
    reserved_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')

    # Test 3 select_comfort_category
    comfort_category = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')

    # Test 4 phone_number
    phone_field = (By.CLASS_NAME, 'np-text')
    input_for_phone = (By.ID, 'phone')
    button_send_phone_number = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button')
    input_for_code = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/input')
    button_confirm_code = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')

    # Test 5 add_card
    button_payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    button_add_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled > div.pp-title')
    card_number_field = (By.ID, 'number')
    card_code_number_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    button_agree_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    check_agree_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    close_pop_up_card_windows = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')


    # Test 6 message_for_driver
    message_for_driver_text = (By.ID, 'comment')

    # Test 7 blanket_is_selected
    blanket_selector = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div')
    blanket_value = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')

    # Test 8 add_2_ice_creams
    ice_cream_plus_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_count = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')


    # Test 9 taxi_request_modal_display
    button_find_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    taxi_driver_is_selected = (By.CSS_SELECTOR, 'order-button')
    header_order_title = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_taxi_request_button(self):
        # Hace Clic en el botón "Pedir un taxi"
        self.driver.find_element(*self.taxi_request_button).click()

    def click_comfort_category(self):
        # Selecciona la tarifa "Comfort".
        self.driver.find_element(*self.comfort_category).click()

    def click_phone_field(self):
        self.driver.find_element(*self.phone_field).click()

    def set_phone_number(self, phone):
        self.driver.find_element(*self.input_for_phone).send_keys(phone)

     # hace en botón "siguiente"
    def click_continue_button(self):
        self.driver.find_element(*self.button_send_phone_number).click()

        # Introducir código

    def add_phone_code(self, code):
        self.driver.find_element(*self.input_for_code).send_keys(code)

        # confirma código

    def click_confirm_button(self):
        self.driver.find_element(*self.button_confirm_code).click()

        # devuelve el valor del phone field

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).text


    def set_steps_payment_method(self, number_card, code_card):
        #clic en el botón de método de pago
        self.driver.find_element(*self.button_payment_method).click()
        # clic en el botón de "añadir una tarjeta"
        self.driver.find_element(*self.button_add_card).click()
        # Agregar el numero de tarjeta
        self.driver.find_element(*self.card_number_field).send_keys(number_card)
        # Enviar el código de la tarjeta
        code_field = self.driver.find_element(*self.card_code_number_field)
        code_field.send_keys(code_card)
        # Hacer TAB para cambiar el enfoque del campo
        code_field.send_keys(Keys.TAB)
        # Hacer clic para guardar la tarjeta nueva
        self.driver.find_element(*self.button_agree_card).click()

    def click_close_pop_up_card_windows(self):
        # Clic para cerrar la ventana emergente del número de teléfono
        self.driver.find_element(*self.close_pop_up_card_windows).click()

    def check_agreed_card(self):
        # confirma que el botón de comfort este seleccionado
        elemento = self.driver.find_element(*self.check_agree_card)
        agree_card = elemento.is_displayed()
        return agree_card

    def set_message_for_driver(self, driver_message):
        # Envia mensaje al conductor
        self.driver.find_element(*self.message_for_driver_text).send_keys(driver_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_text).get_property('value')

    def click_blanket_selector(self):
        # al hacer clic selecciona manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    def click_ice_cream_plus(self):
        # al hacer clic en el botón "+" agrega un helado.
        self.driver.find_element(*self.ice_cream_plus_button).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('innerText')

    def click_find_taxi(self):
        # Hace clic en el botón para buscar un taxi.
        self.driver.find_element(*self.button_find_taxi).click()

    def check_for_button_find_taxi(self):
        # Confirma que el botón de "pedir un taxi" aparezca.
        elemento = self.driver.find_element(*self.button_find_taxi)
        button_find_taxi = elemento.is_displayed()
        return button_find_taxi

    def check_header_order_title(self):
        elemento = self.driver.find_element(*self.header_order_title)
        header_order_title_is_visible = elemento
        return header_order_title_is_visible

    def check_taxi_driver_is_selected(self):
        # Confirma que la imagen del conductor aparezca en la ventana emergente de la ruta.
        elemento = self.driver.find_element(*self.taxi_driver_is_selected)
        taxi_driver_is_selected = elemento.is_displayed()
        return taxi_driver_is_selected


