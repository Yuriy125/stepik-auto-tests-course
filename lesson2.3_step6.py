from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
    button.click()
    
    redirect_page = browser.window_handles[1]
    browser.switch_to.window(redirect_page)
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    a = browser.find_element_by_id("answer").send_keys(y)

    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1000)
    # закрываем браузер после всех манипуляций
    browser.quit()



