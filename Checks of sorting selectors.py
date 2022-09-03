''' Авторизация, проверка выставления селектора "по умолчанию" и сортировки,
смена сортировки на "от дорогого к дешёвому" '''

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")
driver.find_element(By.CSS_SELECTOR, "[href = 'https://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
driver.find_element(By.LINK_TEXT, "Shop").click()
default_order = driver.find_element(By.CSS_SELECTOR, "[value = 'menu_order']")
default = default_order.get_attribute("selected")
if default is not None:
    print("Сортировка 'по умолчанию' выставлена")
else:
    print("Сортировка 'по умолчанию' НЕ выставлена")
ordering = driver.find_element(By.CLASS_NAME, "orderby")
grouping_selection = Select(ordering)
grouping_selection.select_by_value("price-desc")
descending = driver.find_element(By.CSS_SELECTOR, "[value = 'price-desc']").get_attribute("selected")
if descending is not None:
    print("Сортировка 'от дорогого к дешевому' установлена успешно")
else:
    print("Не получилось установить сортировку 'от дорогого к дешевому'")
driver.quit()
