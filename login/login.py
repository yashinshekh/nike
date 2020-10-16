from seleniumwire import webdriver
import json
import csv



if __name__ == '__main__':
    email = "nyasin585@gmail.com"
    password = "123456789aR"

    driver = webdriver.Firefox()
    driver.install_addon("/home/yashin/Documents/fiverr/1extension/hoxx.xpi")
    driver.get("https://www.nike.com/login")


    driver.find_element_by_xpath('.//*[@name="emailAddress"]').send_keys(email)
    driver.find_element_by_xpath('.//*[@name="password"]').send_keys(password)

    driver.find_element_by_xpath('.//input[@value="SIGN IN"]').click()

    for request in driver.requests:
        if 'https://unite.nike.com/login' in request.path:
            print(request.response.body)



