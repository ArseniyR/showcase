'''Проверка наличия на складе вкусняшек для котика:
Вход на сайт PetShop, ввод названия вкусняшек в строку поиска, активация поиска через клавиатуру.
Закрытие всплывающего окошка (iframe), переход на искомую страницу вкусняшек.
Получение информации о наличии/отсутствии товара, вывод в консоли'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.petshop.ru/")
driver.find_element(By.CLASS_NAME, "InputSearch_input__Tmwvh").send_keys("пир охотника")
action = ActionChains(driver)
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
iframe = driver.find_element(By.CLASS_NAME, 'flocktory-widget')
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, '.widget__header .widget__close').click()
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, "[href='/catalog/cats/pauchi-pir-okhotnika-myasnye-kusochki-dlya-koshek-s-utkoy-krolikom-i-dichyu/']").click()
a = driver.find_element(By.CLASS_NAME, "style_delivery_availability__3hZIC").text
print(a)
driver.quit()