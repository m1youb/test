from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.tryhackme.com/login')

username_field = driver.find_element(By.ID, "username-or-email-field")
username_field.send_keys("Fein")

password_field = driver.find_element(By.ID, "password-field")
password_field.send_keys("KhadijaZennouhi@54")

time.sleep(3)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(3)

driver.get('https://tryhackme.com/room/learncyberin25days')

complete = driver.find_element(By.CLASS_NAME, "sc-kAyceB kWIUDX sc-tSoMJ sc-esPSxW jexFtx boBXRI")