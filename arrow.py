from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wb = webdriver.Chrome('./chromedriver.exe')
wb.get('https://designsystem.digital.gov/components/combo-box/')
time.sleep(3)
combo = '/html/body/div[2]/div/main/div/div[2]/div/div/input'
wb.find_element(By.XPATH,combo).click()
time.sleep(0.5)

ActionChains(wb).send_keys(Keys.DOWN).perform()
print('concluido')


