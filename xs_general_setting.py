from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import csv
import os
import requests
from requests import get

#prevent web close****************
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#download
prefs={"download.default_directory":"\download"}
options.add_experimental_option("prefs", prefs)


#********************************************

driver = webdriver.Chrome(service=service, options=options)
    #web IP for 192.168.10.97
driver.get("http://192.168.10.97/#/login")

title = driver.title
driver.implicitly_wait(10)
driver.maximize_window()

#login
def login():
   

    #user input
    text_box = driver.find_element(by=By.CLASS_NAME, value="form-control")
    text_box.send_keys("Admin")
    

    #password input
    #*[@id="uid-xxxxxxxxxx"]
    #/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[2]/div/input
    psword_box = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[2]/div/input')
    psword_box.send_keys("123456")
    time.sleep(5)

    #button submit
    submit_btn = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[5]/div/div[2]/div[1]/button')
    submit_btn.click()

login()



def general_setting():
    sys_setting = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/ul/li[7]/a')
    sys_setting.click()
    time.sleep(3)
    general_setting = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/ul/li[7]/ul/li[1]')
    general_setting.click()
    time.sleep(3)


    #card_heder確認
    try:
        correct_header = ["辨識參數","自動補光設置","平板顯示設定","打卡鐘模式","自定義功能按鈕","平板介面語言","中央管理","平板管理密碼"]
        card_header= driver.find_elements(By.CLASS_NAME, value="h3") 
        card_header = [tmp.text for tmp in card_header]
        time.sleep(5)
        assert card_header == correct_header
        print("card_header=", card_header)   

        print("標題正確!")
        time.sleep(5)

    except AssertionError as title_error:
        title_error = driver.find_elements(By.CLASS_NAME, value="h3") 
        title_error = [tmp.text for tmp in title_error]
        print("title_error", title_error)
        time.sleep(5)



    #辨識參數
    #read table
    #click table 




general_setting()