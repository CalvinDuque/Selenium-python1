import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/v1/")
browser.maximize_window ()
time.sleep(5)

# Find_element() encontra o elemento ID na pagina caso nao encontrar da erro
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# Send_keys() preenche os campos selecionados
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Click() clica no botão selecionado
btn_login.click()

# Text
products_title = browser.find_element(By.XPATH, "//div[@class='product_label']")
print(products_title.text)
assert products_title.text == "Products"

# Get_attribute() mais um comando que interage com o elemento
img_backpack = browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
print(img_backpack.get_attribute("class"))
assert img_backpack.get_attribute("class") == "inventory_item_img"
assert img_backpack.is_displayed #determinado elementro esta presente 
