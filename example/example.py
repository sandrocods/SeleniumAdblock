import SeleniumAdblock
from selenium import webdriver

# Create a new instance of the ChromeOptions class. and start adblock
options = SeleniumAdblock.SeleniumAdblock()._startAdBlock()

# you can add more arguments to the options object
options.add_argument("enable-automation")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-web-security")


# dont add options.add_argument("--disable-extensions") because it will disable the adblock extension


# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Go to a website
driver.get("https://www.detik.com/")
driver.save_screenshot("Clean 🧹.png")