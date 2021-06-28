from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    
    n1 = int(browser.find_element_by_id("num1").text)
    n2 = int(browser.find_element_by_id("num2").text)
    a = str(n1 + n2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(a) # ищем элемент с текстом "Python"
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла


