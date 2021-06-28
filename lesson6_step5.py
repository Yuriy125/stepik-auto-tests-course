import math
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_link_text(a)
link.click()



try:

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Yuriy")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Dementiev")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Tyumen")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла

