from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt

import time
from colorama import Fore
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# service= Service("C:\\Users\\Thndr\\Downloads\\chromedriver_win32\\chromedriver.exe")
def get_driver():
    options=webdriver.ChromeOptions()
    options.add_argument("disable-infobar")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    # options.add_experimental_option("exludeSwitches",["enable-automation"])
    options.add_argument("disabled-blink-features=AutomationControlled")
    
    driver=webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id",value="id_username").send_keys("automated")
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    element=driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
    time.sleep(2)
    text=element.text.split(": ")[1]
    write_file(text=text)

    print(element.text.split(": ")[1])

def write_file(text):
    filename= f"{dt.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt"
    with open(filename,'w') as file:
        file.write(text)

    # print(f"{Fore.GREEN}{driver.current_url}")


main()