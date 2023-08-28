from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class A:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.username = 'Admin'
        self.password = 'admin124'

    def B(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        #self.driver.find_element(by=By.LINK_TEXT, value='/web/index.php/admin/viewAdminModule').click()

        if self.url !=self.driver.current_url:
            print("SUCCESS : LOGIN Successfully ")
        else:
            print("Fail : Login failed !")

        sleep(5)
        self.driver.close()

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

A(url).B()