import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window ()
browser.get("https://chercher.tech/practice/frames")

iframe1 = browser.find_element(By.ID, "frame1") 
browser.switch_to.frame(iframe1) #entramos em outro html dentro da pagina
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iframe1") #escrever dentro do campo escolhido
time.sleep(2)

iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3) #fomos para o irmao do iframe1
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']") #encontra o checkbox e em baixo clica ele
checkbox.click()
time.sleep(2)

browser.switch_to.default_content() #saimos do iframe1

iframe2 = browser.find_element(By.ID, "frame2") 
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(2)

browser.quit()