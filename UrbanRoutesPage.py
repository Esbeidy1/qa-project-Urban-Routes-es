import data
import helpers
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # atributo para hacer click en botón "Pedir un Taxi"
    taxi_request_button = (By.CLASS_NAME, 'round button')

    # atributo para espera después de hacer click en "Pedir un Taxi"
    reserved_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')

    # atributo para elegir categoría "Comfort"
    comfort_category = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer >'
                                         'div.tariff-picker.shown > div.tariff-cards > div.tcard.active')

    # atributo para insertar numero de teléfono
    phone_number_box = (By.CLASS_NAME, 'np-button')
    text_in_phone_number_box = (By.CLASS_NAME, 'np-text')
    input_phone_number_container = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal >'
                                                     'div.section.active > form > div.np-input > div')
    sms_input_box = (By.CLASS_NAME, 'input-container')
    sms_confirmation_button = (By.CLASS_NAME, 'button full')

    # atributos para agregar método de pago:
    button_payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer >'
                                              'div.tariff-picker.shown > div.form > div.pp-button.filled')
    button_add_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active >'
                                        'div.pp-selector > div.pp-row.disabled')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_number_field = (By.CLASS_NAME, 'input-container')
    button_agree_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual >'
                                          'div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    check_agree_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active >'
                                         'div.pp-selector > div:nth-child(3)')
    close_pop_up_card_windows = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal >'
                                                  'div.section.active > button')

    # atributo para agregar mensaje para el conductor:
    message_for_driver_text = (By.ID, 'comment')

    # atributos para seleccionar opción Pedir una manta y pañuelos:
    blanket_selector = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown >'
                         'div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown >'
                         'div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown >'
                         'div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')

    # Atributos para pedir 2 helados:
    ice_cream_plus_button = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown >'
                         'div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) >'
                         'div > div.r-counter > div > div.counter-plus')
    ice_cream_count = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form >'
                         'div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) >'
                         'div > div.r-counter > div > div.counter-value')

    # Atributos para esperar a que la información del conductor en el modal aparezca:
    button_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
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
        # Hacer Clic en el botón "Pedir un taxi"..
        self.driver.find_element(*self.taxi_request_button).click()

    def click_comfort_category(self):
        # Seleccionar la tarifa "Comfort".
        self.driver.find_element(*self.comfort_category).click()

    def fill_phone_number(self):
        # Rellena el número de teléfono.
        self.driver.find_element(*self.phone_number_box).click()
        helpers.standard_wait_time(self)
        # Clic en el campo para introducir el número de teléfono
        self.driver.find_element(*self.input_phone_number_container).click()
        # Introduce el número de teléfono en el campo
        self.driver.find_element(*self.input_phone_number_container).send_keys(data.phone_number)
        # Hacer clic en el botón "Siguiente" de la ventana "Introduce tu número"
        self.driver.find_element(By.CLASS_NAME, 'button full').click()
        helpers.standard_wait_time(self)
        # Colocar el código SMS
        self.driver.find_element(*self.sms_input_box).click()
        self.driver.find_element(*self.sms_input_box).send_keys(helpers.retrieve_phone_code())
        helpers.standard_wait_time(self)
        self.driver.find_element(*self.sms_confirmation_button).click()

    def set_steps_payment_method(self, number_card, code_card):
        # clic en el botón de método de pago
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
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.button_agree_card))
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
        # Enviar mensaje al conductor
        self.driver.find_element(*self.message_for_driver_text).send_keys(driver_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_text).get_property('value')

    def click_blanket_selector(self):
        # Hacer clic para seleccionar manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    def click_ice_cream_plus(self):
        # Hacer clic en el botón "+" para agregar un helado.
        self.driver.find_element(*self.ice_cream_plus_button).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('innerText')

    def click_find_taxi(self):
        # Hacer clic en el botón para buscar un taxi.
        self.driver.find_element(*self.button_find_taxi).click()

    def check_for_button_find_taxi(self):
        # Confirma que el botón de buscar un taxi apareció.
        elemento = self.driver.find_element(*self.button_find_taxi)
        button_find_taxi = elemento.is_displayed()
        return button_find_taxi

    def check_header_order_title(self):
        # Confirma que el encabezado aparezca en la ventana emergente.
        elemento = self.driver.find_element(*self.header_order_title)
        header_order_title_is_visible = elemento
        return header_order_title_is_visible

    def check_taxi_driver_is_selected(self):
        # Confirma que la imagen del conductor aparezca en la ventana emergente de la ruta.
        elemento = self.driver.find_element(*self.taxi_driver_is_selected)
        taxi_driver_is_selected = elemento.is_displayed()
        return taxi_driver_is_selected

  #  def click_taxi_request_button(self):
   #     pass
