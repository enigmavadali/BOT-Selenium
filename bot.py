from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=sur.vad.rt15@rait.ac.in&wantsurl=")
password = "dypatil@123"
pass_box = driver.find_element_by_id("password")
pass_box.send_keys(password)
#pass_box.send_keys(Keys.RETURN)
pass_box.submit()
time.sleep(2)
# OR
# login_button = driver.find_element_by_id("loginbtn")
# login_button.click()

dashboard = driver.window_handles[0]
for subject in driver.find_elements_by_class_name("launchbutton"):
    subject.click()

for tab in range(len(driver.window_handles)-1,-1,-1):
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(3)
    link = driver.find_element_by_xpath('//*[@id="inst50217"]/div[2]/a/div/span')
    link.click()
    time.sleep(3)
    urls = driver.find_elements_by_class_name("pending")

    #urls = driver.find_elements_by_xpath('//*[@id="gridiconcontainer"]/ul/li/div/ul/li/p/a')
    for url in urls:
        driver.execute_script("window.open(arguments[0]);",url.get_attribute("href"))
        driver.switch_to.window(driver.window_handles[7])
        time.sleep(4)
        driver.close()
        driver.switch_to.window(driver.window_handles[tab])

driver.quit()
