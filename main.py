from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
serv_obj= Service('chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.set_window_size(700,800)


q = '� This is the most powerful flashlight in the world� Amazing Super Bright�Flashlight��'

driver.get('https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&q=' + q + '&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all')
time.sleep(2)

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True


