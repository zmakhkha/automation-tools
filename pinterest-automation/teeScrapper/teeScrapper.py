import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv
import os
from utils import read_urls

def save_csv(csv_path, path,title, desc, urls):
   with open(csv_path, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Title", "Path", "Description", "url"])
      for i in range(len(title)):
         row = [title[i], os.path.abspath(path[i]), desc[i], urls[i]]
         writer.writerow(row)
    
def openPages(urlLst):
   driver.switch_to.window(driver.window_handles[0])
   for i in range(len(urlLst)):
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[i + 1])
      driver.get(urlLst[i])
      print(urlLst[i])
      sleep(2)
   driver.switch_to.window(driver.window_handles[0])

def downOrigImg(imgPaths, folPath):
   closed = 0
   paths = []
   for i in range(len(imgPaths)):
      driver.switch_to.window(driver.window_handles[i + 1 - closed])
      l = driver.find_element(By.CSS_SELECTOR, 'body > img')
      path = folPath + "/" + str(i) + 'img.png'
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
   descs = []
   for i in range(len(urlLst)):
      driver.switch_to.window(driver.window_handles[i + 1 - closed])
      title = driver.find_element(By.CSS_SELECTOR, '#content > div.m-design > div:nth-child(1) > div > div.m-design__product > div.m-design__title > h1').text
      titles.append(title)
      desc = driver.find_element(By.CSS_SELECTOR, '#content > div.m-design > div:nth-child(1) > div > div.m-design__product > div.m-design__title > div > h2').text
      descs.append(desc)
      l = driver.find_element(By.CSS_SELECTOR, '#content > div.m-design > div:nth-child(1) > div > div.m-design__product > div.m-design__preview > div > div.m-product-preview__main.jsProductMainImages > div.glide.m-product-preview__glider.jsProductImgGlide.glide--slider.glide--horizontal > div.glide__track.m-product-preview__glider-track > ul > li.glide__slide.m-product-preview__glider-slide.active > picture > img')
      print(l.get_attribute("src"))
      imgUrls.append(l.get_attribute("src"))
      driver.execute_script("window.close('');")
      closed += 1
      sleep(3)
   return imgUrls, titles, descs
   
def openOriginImgs(imgs):
   for i in range(len(imgs)):
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[i + 1])
      driver.get(imgs[i])
      sleep(1)
   driver.switch_to.window(driver.window_handles[0])
      

if __name__ == "__main__":
   if len(sys.argv) != 4:
      print("Usage: python script.py <imgFolder> <urls> <csv_path>")
      sys.exit(1)
   upDir = "img"
   options = Options()
   options.add_experimental_option("excludeSwitches", ["enable-logging"])
   driver = webdriver.Chrome(options=options)
   print("testing started")
   
   allUrls = read_urls(sys.argv[2])
   print("opened all urls")
   openPages(allUrls)
   print("got all urls")
   allUrls, allTitles, allDescs = getInfo(allUrls)
   print("before opening images")
   print(allUrls)
   print("----------------")
   #openOriginImgs(allUrls)
   openPages(allUrls)
   print("after opening images")
   imgPaths = downOrigImg(allUrls, sys.argv[1])
   print(imgPaths)
   print(allTitles)
   allUrls = read_urls(sys.argv[2])
   save_csv(sys.argv[3], imgPaths, allTitles, allDescs, allUrls)
   