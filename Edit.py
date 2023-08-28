from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class A:

    def __init__(self):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.username = 'Admin'
        self.password = 'admin123'

    def B(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[2]/i').click()

        Nickname = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')))
        Nickname.send_keys('C')

        sleep(3)

        Save = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')))
        Save.click()
        sleep(2)

        Save_1 = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')))
        Save_1.click()

        sleep(3)

        Employee = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')))
        Employee.click()

        print('Employee Edited Successfully')
        sleep(3)
        self.driver.close()

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

A().B()