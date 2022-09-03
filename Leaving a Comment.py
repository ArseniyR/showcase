'''Вход на сайт, скролл страницы, открыть страницу товара, добавить комментарий'''

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element(By.CSS_SELECTOR, '[title="Selenium Ruby"]')
selenium_ruby.click()
driver.find_element(By.CLASS_NAME, "reviews_tab").click()
driver.find_element(By.ID, "comment").send_keys("Nice book!")
driver.find_element(By.ID, "author").send_keys("Matthew")
driver.find_element(By.ID, "email").send_keys("matthewgig@gmail.com")
driver.find_element(By.ID, "submit").click()
driver.quit()


