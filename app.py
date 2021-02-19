import os
import names
import random
import time, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://wn.nr/Qmhkkc"

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

while True:
  login_email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[1]/div/ul/li[2]/a")))
  login_email.location_once_scrolled_into_view
  login_email.click()

  input_full_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input')))
  input_full_name.send_keys(names.get_full_name())

  input_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input')))
  input_email.send_keys(names.get_first_name().lower()+"_" + names.get_last_name().lower() +"@gmail.com")

  btn_cont = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div[6]/div[2]/div[2]/div/form/div/span[1]/button/span[2]')))
  btn_cont.click()

  subs = ["em5433464","em5433785","em5433793","em5433809"]
  rand_sub = random.choice(subs)
  btn_subs = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="' + rand_sub +'"]/a')))
  driver.execute_script("arguments[0].click();", btn_subs)

  btn_cont2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="' + rand_sub +'"]/div/div/form/div[2]/div/a')))
  driver.execute_script("arguments[0].click();", btn_cont2)

  while True:
    checked = driver.find_element_by_xpath('//*[@id="current-entries"]/span[1]')
    if checked.text == '30':
      break
    time.sleep(3)

  btn_logout = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div[6]/div[2]/div[3]/div/span/div[1]/div[2]/a[2]')))
  btn_logout.location_once_scrolled_into_view
  btn_logout.click()
  time.sleep(random.randint(1,3))