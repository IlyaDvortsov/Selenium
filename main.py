import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Ожидание, пока цена дома не станет $100
    wait = WebDriverWait(browser, 12)
    price_element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решение математической задачи (используйте ваш предыдущий код)
    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)
    result = calc(x)

    browser.find_element(By.ID, "answer").send_keys(result)

    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)  # Пауза для просмотра результата
    browser.quit()

