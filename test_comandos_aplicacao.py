import time
from selenium import webdriver

browser = webdriver.Chrome()

#title
browser.get("https://www.saucedemo.com/v1/")
time.sleep(3) 
print("O titulo da pagina é:", browser.title) #imprimi o titulo da pagina

#current_url
print("A URL da pagina é:", browser.current_url) #imprimi a URL da pagina

#page_source
print("O codigo-fonte da página é:", browser.page_source) #imprimi o codigo fonte da pagina

browser.quit()