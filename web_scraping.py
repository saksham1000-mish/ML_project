import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import io
from PIL import Image
import requests
import time
import urllib

path = ""

cService = webdriver.ChromeService(executable_path='C:\\Users\\saksh\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service = cService)

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/saksh/Library/Application Support/Google/Chrome/Default')
# options.add_argument('--headless')
driver = uc.Chrome(options=options)
driver.minimize_window()

url='https://www.google.com/search?sca_esv=28e9cba476193d42&udm=2&sxsrf=ADLYWIKiPR1rHLqLd-1LAJbU5YHBJHMsrQ:1717482816867&q=open+tap+wastage&spell=1&sa=X&ved=2ahUKEwjH2tOJqsGGAxXxU2wGHc0VBTAQBSgAegQIBxAB&biw=1707&bih=811&dpr=1.13'
driver.get(url)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

# YQ4gaf kn3ccd VQAsE

img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'YQ4gaf')]")

image_urls = []
for img in img_results:
    image_urls.append(img.get_attribute('src'))

folderPath = "C:\\Users\\saksh\\OneDrive\\Desktop\\ML Projects\\Public Grievances(NICSI)\\data\\openTaps"


for i in range(8,100):
    urllib.request.urlretrieve(str(image_urls[i]), folderPath+"taps_{}.jpg".format(i))

driver.quit()