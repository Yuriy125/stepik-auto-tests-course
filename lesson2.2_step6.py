from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    a = browser.find_element_by_id("answer").send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 150);")
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла

