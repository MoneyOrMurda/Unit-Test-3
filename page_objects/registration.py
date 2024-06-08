from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    EMAIL_INPUT = (By.ID, 'register_email')
    PASSWORD_INPUT = (By.ID, 'register_password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'register_confirm_password')
    FIRSTNAME_INPUT = (By.ID, 'register_firstname')
    LASTNAME_INPUT = (By.ID, 'register_lastname')
    TELEPHONE_INPUT = (By.ID, 'register_telephone')
    COUNTRY_DROPDOWN = (By.ID, 'register_country_id')
    COUNTRY_OPTION = (By.XPATH, "//option[@value='176']")
    ZONE_DROPDOWN = (By.ID, 'register_zone_id')
    ZONE_OPTION = (By.XPATH, "//option[@value='83']")
    CITY_INPUT = (By.ID, 'register_city')
    POSTCODE_INPUT = (By.ID, 'register_postcode')
    ADDRESS_INPUT = (By.ID, 'register_address_1')
    CONFIRM_BUTTON = (By.ID, 'simpleregister_button_confirm')

    def fill_registration_form(self, email, password, firstname, lastname, telephone, city, postcode, address):
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.find_element(self.FIRSTNAME_INPUT).send_keys(firstname)
        self.find_element(self.LASTNAME_INPUT).send_keys(lastname)
        self.find_element(self.TELEPHONE_INPUT).send_keys(telephone)
        self.find_element(self.COUNTRY_DROPDOWN).click()
        self.find_element(self.COUNTRY_OPTION).click()
        self.find_element(self.ZONE_DROPDOWN).click()
        self.find_element(self.ZONE_OPTION).click()
        self.find_element(self.CITY_INPUT).send_keys(city)
        self.find_element(self.POSTCODE_INPUT).send_keys(postcode)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        self.find_element(self.CONFIRM_BUTTON).click()
