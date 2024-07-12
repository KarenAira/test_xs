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

#UI for xs
def UI_xs():
 
    title = driver.title
    driver.implicitly_wait(10)

    #左側功能欄
    def test_element_clickable():
        correct_functions = ["日出勤", "月出勤", "出勤設定",
                        "出勤操作", "人員報表", "訪客報表", "調查", "人員", "訪客", "群組", "門禁管理", "門禁裝置設定", "遠端觸發", "事件管理", 
                        "迎賓看板", "點名看板", "容留看板", "一般設定","結果提示" "帳號管理", "時間設置", "網路設定", "備份與還原", "軟體更新", "系統重設", "系統日誌"]
        side_function = driver.find_element(by=By.CSS_SELECTOR, value='ul.c-sidebar-nav.h-100.ps')
        time.sleep(5)
        side_function = [tmp.text for tmp in side_function.find_elements(By.CSS_SELECTOR, "li.c-sidebar-nav-item")]
        time.sleep(5)
        try:
            assert side_function == correct_functions
            print("Left sidebar all correct!")
            time.sleep(5)

        except AssertionError as e:
            print(e)
            time.sleep(5)

    test_element_clickable()
    print("Left sidebar all correct!")
    time.sleep(10)
    
    #出勤
    def attendance():
        sidebar= driver.find_element(by=By.LINK_TEXT, value="出勤")
        sidebar.click()
    attendance()

    #daily attendance
    def daily_attend():
        sidebar_daily = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/ul/li[1]/ul/li[1]/a')
        sidebar_daily.click()
    daily_attend()

     #add person

    #Export excel_daily
    def daily_export():
        excel_exp = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
        excel_exp.click()
        driver.implicitly_wait(10)
        time.sleep(10)

        #export setting & export          
        export_download= driver.find_element(by=By.CLASS_NAME, value='btn.ml-1.btn-temp.btn-primary')
        export_download.click()
        driver.implicitly_wait(10)
        time.sleep(10)

        #finish download and close setting window
        close_setting =driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/main/div/div/div/div/div/div[4]/div[1]/div/div/footer/button[1]')
        close_setting.click()
        driver.implicitly_wait(10)
        time.sleep(10)

    daily_export()
                            
    
    #monthly atterdance
    def month_attend():
        sidebar_monthly = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/ul/li[1]/ul/li[2]/a')
        sidebar_monthly.click()
        time.sleep(10)

    month_attend()
    

    #Export excel_daily
    def monthly_export():
        excel_exp = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
        excel_exp.click()
        time.sleep(10)

        #export setting & export   
        month_export_download= driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/main/div/div/div/div/div/div[4]/div[1]/div/div/footer/button[2]')
        month_export_download.click()
        time.sleep(10)

        #finish download and close setting window
        close_setting = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/main/div/div/div/div/div/div[4]/div[1]/div/div/footer/button[1]')
        close_setting.click()
        time.sleep(2)
        
    monthly_export()

UI_xs()





