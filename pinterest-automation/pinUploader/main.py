from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


login_ = "dummy"
pass_ = "pass"
url = "https://www.pinterest.fr/business/login/"


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("testing started")
driver = webdriver.Chrome(options=options)
driver.get(url)
sleep(3)

def logMeIn(_login, _pass):
	print("[logMeIn] scoop")
	driver.find_element(By.ID, "email").send_keys(login_)
	sleep(2)
	driver.find_element(By.ID, "password").send_keys(pass_)
	sleep(2)
	driver.find_element(By.CSS_SELECTOR, '#mweb-unauth-container > div > div:nth-child(3) > div > div > div:nth-child(3) > form > div:nth-child(7) > button').click()
	sleep(7)
	title = driver.title
	# Test if title is correct
	# assert "Pinterest" in title
	# print("TEST 0: `title` test passed")




def main():
    logMeIn(login_, pass_)
    sleep(7)

driver.quit()
    
if __name__ == "__main__":
    main()