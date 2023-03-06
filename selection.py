from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wb = webdriver.Chrome('./chromedriver.exe')
wb.get('https://designsystem.digital.gov/components/combo-box/')
time.sleep(3)
combo = '/html/body/div[2]/div/main/div/div[2]/div/div/select'
sel = Select(wb.find_element(By.XPATH,combo))

sel.select_by_visible_text("Cherry")
time.sleep(0.8)
#select by select_by_index() method
#~ sel.select_by_index(0)
print('concluido')


