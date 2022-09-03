''' Проверка полного процесса покупки товара:
вход на сайт, скролл, переход на страницу товара, добавление в корзину.
Переход в корзину, заполнение обязательных полей, выбор способа оплаты.
Проверка сообщения "Your order has been received." '''

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
import time
driver.get("http://practice.automationtesting.in/")
driver.find_element(By.LINK_TEXT, "Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.CSS_SELECTOR, "[data-product_id = '182']").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
time.sleep(1)
checkout = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/checkout/']")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(checkout))
checkout.click()
first_name_input = driver.find_element(By.ID, "billing_first_name")
wait.until(EC.element_to_be_clickable(first_name_input))
first_name_input.send_keys("Matthew")
driver.find_element(By.ID, "billing_last_name").send_keys("Seppuku")
driver.find_element(By.ID, "billing_email").send_keys("britishenglish@bk.ru")
driver.find_element(By.ID, "billing_phone").send_keys("+7 (999) 999-9999")
driver.find_element(By.CLASS_NAME, "select2-chosen").click()
driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Ireland")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "select2-result-label").click()
time.sleep(1)
driver.find_element(By.ID, "billing_address_1").send_keys("Ale Street")
driver.find_element(By.ID, "billing_city").send_keys("Dublin")
driver.find_element(By.ID, "billing_state").send_keys("Dublin")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element(By.ID, "payment_method_cheque").click()
driver.find_element(By.ID, "place_order").click()
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method > strong"), "Check Payments"))
time.sleep(1)
driver.quit()