## web control
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep
import keyboard

## keyborad control
import pyautogui as p

from selenium.webdriver.firefox.options import Options


# Initialize the driver with the profile
driver = webdriver.Firefox()
driver.get("https://typing.twi1.me/game/294913")
# 2. 要素がクリック可能になるまで待つ
ok_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "mtjIc-check"))
)
driver.execute_script("window.scrollTo(0, 100)")

check_btn = driver.find_element(By.CLASS_NAME, "mtjIc-check")

driver.find_element(By.CLASS_NAME, "mtjIc-check").click()

start_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "mtjIc-start"))
)

driver.find_element(By.CLASS_NAME, "mtjIc-start").click()
p.sleep(1)
p.press("space")

now_ipt = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "mtjNowInput"))
)
while True:
    parent1 = driver.find_element(By.CLASS_NAME, "mtjGmSc-roma")
    now_input = parent1.find_element(By.CLASS_NAME, "mtjNowInput").text
    if now_input:
        p.press(now_input)
    else:
        break
    if keyboard.is_pressed("esc"):
        print("loop quited")
        break
sleep(10000)
driver.close()