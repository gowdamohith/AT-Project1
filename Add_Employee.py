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
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()

        First = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')))
        First.send_keys('A')

        Middle = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')))
        Middle.send_keys('B')

        Last = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')))
        Last.send_keys('C')
        sleep(3)
        Save = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))
        Save.click()

        Nickname = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')))
        Nickname.send_keys('cvb')

        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys(
            '123456789')
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input').send_keys(
            '687354987')
        sleep(3)

        Save_1 = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,
                                                                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')))
        Save_1.click()

        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()


        print('Employee added Successfully')

        sleep(5)
        self.driver.close()

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

A().B()