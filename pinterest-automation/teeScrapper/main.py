import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def read_urls(filename):
    lines = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

def openPages(urlLst):
   driver.switch_to.window(driver.window_handles[0])
   for i in range(len(urlLst)):
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[i + 1])
      driver.get(urlLst[i])
      sleep(1)
   driver.switch_to.window(driver.window_handles[0])

def downOrigImg(imgPaths):
   closed = 0
   paths = []
   for i in range(len(imgPaths)):
      driver.switch_to.window(driver.window_handles[i + 1 - closed])
      l = driver.find_element(By.CSS_SELECTOR, 'body > img')
      path = str(i) + 'img.png'
      with open(path, 'wb') as file:
         file.write(driver.find_element(By.CSS_SELECTOR, 'body > img').screenshot_as_png)
      paths.append(path)
      driver.execute_script("window.close('');")
      closed += 1
      sleep(1)
   return paths

def getInfo(urlLst):
   closed = 0
   imgUrls =[]
   titles = []
   for i in range(len(urlLst)):
      driver.switch_to.window(driver.window_handles[i + 1 - closed])
      title = driver.find_element(By.CSS_SELECTOR, '#content > div.m-design > div:nth-child(1) > div > div.m-design__product > div.m-design__title > h1').text
      titles.append(title)
      l = driver.find_element(By.CSS_SELECTOR, '#content > div.m-design > div:nth-child(1) > div > div.m-design__product > div.m-design__preview > div > div.m-product-preview__main.jsProductMainImages > div.glide.m-product-preview__glider.jsProductImgGlide.glide--slider.glide--horizontal > div.glide__track.m-product-preview__glider-track > ul > li.glide__slide.m-product-preview__glider-slide.active > picture > img')
      print(l.get_attribute("src"))
      imgUrls.append(l.get_attribute("src"))
      driver.execute_script("window.close('');")
      closed += 1
      sleep(3)
   return imgUrls, titles

def runAll(url):
   print("testing started")
   openPages(url)
   imgu_urls, titls = getInfo(url)
   print("before opening images")
   print(imgu_urls)
   print("----------------")
   #openOriginImgs(imgu_urls)
   openPages(imgu_urls)
   print("after opening images")
   imgPaths = downOrigImg(imgu_urls)
   print(imgPaths)
   
def openOriginImgs(imgs):
   for i in range(len(imgs)):
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[i + 1])
      driver.get(imgs[i])
      sleep(1)
   driver.switch_to.window(driver.window_handles[0])
      

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("Usage: python script.py <filename>")
      sys.exit(1)
   upDir = "img"
   options = Options()
   options.add_experimental_option("excludeSwitches", ["enable-logging"])
   driver = webdriver.Chrome(options=options)
   allUrls = read_urls(sys.argv[1])
   runAll(allUrls)
   