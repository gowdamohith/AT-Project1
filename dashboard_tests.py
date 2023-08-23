import json
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.login_page_class import HrmLoginPage
from selenium import webdriver

from orangehrmpages.utilities.utils import wait_for_dashboard


# import os

class LoginPageTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Launching my chrome browser before all my test cases start running")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        json_file_path = "/DataSource/test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    @classmethod
    def tearDownClass(cls) -> None:
        print("I am after the test class")

    def test_successfull_login(self):
        hrmpobject = HrmLoginPage(self.driver)
        hrmpobject.input_username(self.data_dict.get("Login_test_data").get("correct_user_name"))
        hrmpobject.input_password(self.data_dict.get("Login_test_data").get("correct_password"))
        hrmpobject.click_login_button()
        assert wait_for_dashboard(self.driver)
        logout_of_hrm(self.driver)

    def test_wrong_username(self):
        hrmpobject = HrmLoginPage(self.driver)
        hrmpobject.input_username(self.data_dict.get("Login_test_data").get("incorrect_user_name"))
        hrmpobject.input_password(self.data_dict.get("Login_test_data").get("correct_password"))
        hrmpobject.click_login_button()
        assert hrmpobject.verify_invalid_cred_locator_presence()


    # def test_wrong_password(self):
    #     hrmpobject = HrmLoginPage(self.driver)
    #     hrmpobject.input_username('Admin')
    #     hrmpobject.input_password('Admin123')
    #     hrmpobject.click_login_button()


