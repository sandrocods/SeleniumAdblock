import time
import unittest
import SeleniumAdblock
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSeleniumAdblock(unittest.TestCase):


    def test_adblock(self):
        self.option = SeleniumAdblock.SeleniumAdblock()._startAdBlock()
        self.option.add_argument("enable-automation")
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.get("https://www.detik.com/")
        self.driver.save_screenshot("Clean.png")

    def test_popupblocker(self):
        self.option = SeleniumAdblock.SeleniumAdblock()._startAdBlock()
        self.option.add_argument("enable-automation")
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.get("https://webbrowsertools.com/popup-blocker/")
        self.driver.find_element(By.XPATH, "//*[@id='popup']/tbody[1]/tr[2]/td[1]/input").click()
        time.sleep(3)
        self.driver.save_screenshot("Popup.png")




if __name__ == '__main__':
    unittest.main()
