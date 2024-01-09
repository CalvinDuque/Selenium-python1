import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/v1/")
browser.maximize_window ()
time.sleep(5)


# Find_element() encontra o elemento ID na pagina caso nao encontrar da erro
# username = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

# send_keys
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

# Find_elements()
auth_fields = browser.find_elements(By.XPATH, "//*[@class='form_input']")
print(auth_fields)
print(len(auth_fields))
assert len(auth_fields) == 5, "O numero de elementos é diferente"
time.sleep(3)

browser.quit()