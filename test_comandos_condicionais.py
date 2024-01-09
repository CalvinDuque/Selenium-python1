import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")
time.sleep(5)

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

# is_displayed()
print(username.is_displayed())
assert username.is_displayed()

# is_enabled() enquanto nao preenche username ou password o botao sign in deveria esta desabilitado
print(username.is_enabled())
assert username.is_enabled()

# is_selected() conferir se o flexbox esta selecionado, como inicialmente ele vem nao selecionado colocamos not, para dar false pois nao foi clicado no flexbox
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

# clicamos no checkbox
checkbox_remember_me.click()

# is_selected confere o flexbox, como selcionamos ele acima vai dar true
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()

browser.quit()