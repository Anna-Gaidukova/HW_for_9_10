from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

'''
На сайте YouTube есть кнопка "Подписаться", которая становится доступной после просмотра видеоролика.
Этот тест проверяет, что кнопка "Подписаться" недоступна, пока видеоролик не будет просмотрен.
 Затем тест ожидает 10 секунд, чтобы кнопка стала доступной. 
После этого тест снова проверяет, что кнопка доступна.
'''

options = ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(4)


    # відкрити сторінку YouTube
driver.get("https://www.youtube.com")

    # знайти відео
video = driver.find_element(By.ID, "video-title")
video.click()

    # чекати доти, доки кнопка стане доступна
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "subscribe-button")))
time.sleep(5)

    # перевірити, чи доступна кнопка
assert driver.find_element(By.ID, "subscribe-button").is_enabled()
time.sleep(5)

driver.quit()
print("Browser exit!")