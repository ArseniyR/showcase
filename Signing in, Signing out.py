'''Авторизация пользователя, проверка перехода в личный кабинет, выход из аккаунта'''

from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.find_element(By.CSS_SELECTOR, '[href="https://practice.automationtesting.in/my-account/"]').click()
driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
sign_out = driver.find_element(By.CSS_SELECTOR, "[href = 'https://practice.automationtesting.in/my-account/customer-logout/']")
assert sign_out.is_displayed()
sign_out.click()
driver.quit()
