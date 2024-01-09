import time
from selenium import webdriver

browser = webdriver.Chrome()

# Get() abre a pagina
browser.get("https://google.com")
time.sleep(2)

# Maximize_window() maximiza a pagina
browser.maximize_window()
time.sleep(2)

# Refresh() atualiza a pagina
browser.refresh()
time.sleep(2)

browser.get("https://www.saucedemo.com/v1/")
time.sleep(2)

# Back() retorna a pagina de origem
browser.back()
time.sleep(2)

# Forward() retona a pagina que estava e volta depois para a pagina
browser.forward()
time.sleep(2)

# #abrir uma nova aba
# browser.switch_to.new_window("tab")
# time.sleep(2)

# # Close() fecha somente uma aba
# browser.close()
# time.sleep(2)

# Quit() fecha tudo
browser.switch_to.new_window("tab")
time.sleep(2)
browser.switch_to.new_window("tab")
time.sleep(2)

browser.quit()