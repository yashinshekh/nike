#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python - BrowserMob - WebDriver"""
from browsermobproxy import Server
from selenium import webdriver
import json
import time


email = "nyasin585@gmail.com"
password = "123456789aR"

class CreateHar(object):
    """create HTTP archive file"""

    def __init__(self, mob_path,email,password):
        """initial setup"""
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None
        self.email = email
        self.password = password

    @staticmethod
    def __store_into_file(title, result):
        """store result"""
        har_file = open(title + '.har', 'w')
        har_file.write(str(result))
        har_file.close()

    def __start_server(self):
        """prepare and start server"""
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self):
        """prepare and start driver"""
        profile = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        self.driver = webdriver.Firefox(firefox_profile=profile)

    def start_all(self):
        """start server and driver"""
        self.__start_server()
        self.__start_driver()

    def create_har(self, title, url):
        """start request and parse response"""
        self.proxy.new_har(ref=title,options={'captureHeaders': True,'captureCookie':True})
        # self.proxy.new_har(title)
        self.proxy.remap_hosts(address="https://unite.nike.com/login?appVersion=833&experienceVersion=833")
        self.driver.get(url)
        self.driver.find_element_by_xpath('.//*[@name="emailAddress"]').send_keys(self.email)
        self.driver.find_element_by_xpath('.//*[@name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('.//*[@value="SIGN IN"]').click()
        time.sleep(14)
        result = json.dumps(self.proxy.har, ensure_ascii=False)
        self.__store_into_file(title, result)

    def stop_all(self):
        """stop server and driver"""
        self.server.stop()
        self.driver.quit()


if __name__ == '__main__':
    path = "browsermob-proxy-2.1.4/bin/browsermob-proxy"
    RUN = CreateHar(path,email,password)
    RUN.start_all()
    RUN.create_har('nike', 'https://www.nike.com/login')
    RUN.stop_all()