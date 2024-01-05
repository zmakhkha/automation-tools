from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import sys
import csv

from utils import read_urls

url = "https://www.pinterest.fr/business/login/"
newPin = "https://www.pinterest.fr/pin-creation-tool/"

class Design:
    def __init__(self, path, title, desc, url):
        self.path = path
        self.title = title
        self.desc = desc
        self.url = url

def read_csv(csv_path):
    objects = []

    with open(csv_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            # Assuming the order of columns is path, title, desc
            title, path, desc, url = row
            obj = Design(path, title, desc, url)
            objects.append(obj)
    return objects

def intiDriver():
	options = Options()
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	print("testing started")
	driver = webdriver.Chrome(options=options)
	return driver
sleep(7)
def logMeIn(driver, _login, _pass):
	driver.get(url)
	print("[logMeIn] scoop")
	sleep(5)
	driver.find_element(By.ID, "email").send_keys(login_)
	sleep(2)
	driver.find_element(By.ID, "password").send_keys(pass_)
	sleep(5)
	driver.find_element(By.CSS_SELECTOR, '#mweb-unauth-container > div > div:nth-child(3) > div > div > div:nth-child(3) > form > div:nth-child(7) > button').click()

board_shirt_gift_idea = '.Cii > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'

def upPins(driver, objLst):
    for i in range(len(objLst)):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(newPin)
        sleep(7)
        input = driver.find_element(By.ID, 'storyboard-upload-input')
        input.send_keys(objLst[i].path)
        sleep(7)
        driver.find_element(By.ID, 'storyboard-selector-title').send_keys(objLst[i].title)
        driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block').send_keys(objLst[i].desc)
        driver.find_element(By.ID, 'WebsiteField').send_keys(objLst[i].url)
        sleep(7)
        driver.find_element(By.CSS_SELECTOR, '.qF5 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
        sleep(7)
        driver.find_element(By.CSS_SELECTOR, board_shirt_gift_idea).click()
        sleep(7)
        #driver.find_element(By.CSS_SELECTOR, '.Il7 > div:nth-child(1)').click()
        #sleep(7)


        
        
        


def runAll(objLst):
    driver = intiDriver()
    logMeIn(driver, login_, pass_)
    sleep(7)
    upPins(driver, objLst)
    sleep(7)
    sleep(50)
    driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
      print("Usage: python script.py <login> <password> <csv_file>")
      sys.exit(1)
    login_ = sys.argv[1]
    pass_ = sys.argv[2]
    dataObjs = read_csv(sys.argv[3])
    runAll(dataObjs)
    
