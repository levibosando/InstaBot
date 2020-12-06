from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep

class InstaBot:

    def __init__(self, data):
        self.driver = webdriver.Firefox()
        self.username = data['username']
        self.password = data['password']


    def login(self):
        self.driver.get("https://instagram.com")
        sleep(2)
        assert "instagram" in self.driver.current_url
        login_username = self.driver.find_element_by_name("username")
        login_username.clear()
        login_username.send_keys(self.username)
        login_password = self.driver.find_element_by_name("password")
        login_password.clear()
        login_password.send_keys(self.password)
        login_password.send_keys(Keys.RETURN)
        sleep(3)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def get_followers(self):
        """This program accesses into your account profile to check followers"""
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]").format(self.username)
        


if __name__ == "__main__":
    with open('config.json') as f:
        data = json.load(f)
    bot = InstaBot(data)
    bot.login()
