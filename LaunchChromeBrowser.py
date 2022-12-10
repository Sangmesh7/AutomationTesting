

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
# drivers will call browsers
# create service object, chrome service, send service object as a property to chrome

service_obj = Service(r'C:\Users\Hp\Desktop\WebDrivers\Chromedriver\Chromedriver.exe')

driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome(executable_path='C:/WebDrivers/Chromedriver/to/Chromedriver.exe')

#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/")
time.sleep(10)
driver.close()
