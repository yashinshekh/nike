from browsermobproxy import Server
import psutil
import time

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == "browsermob-proxy":
        proc.kill()

dict = {'port': 8090}
server = Server(path="./BrowserMobProxy/bin/browsermob-proxy", options=dict)
server.start()
time.sleep(1)
proxy = server.create_proxy()
time.sleep(1)
from selenium import webdriver
profile = webdriver.FirefoxProfile()
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://www.google.co.uk")
print (proxy.har) # returns a HAR JSON blob

server.stop()
driver.quit()