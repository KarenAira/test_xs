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

#prevent web close
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#download
prefs={"download.default_directory":"\download"}
options.add_experimental_option("prefs", prefs)



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

    #sidebar click
    #出勤
    def attendance():
        sidebar= driver.find_element(by=By.LINK_TEXT, value="出勤")
        sidebar.click()
    attendance()
    
                            
    #monthly atterdance
    def month_attend():
        sidebar_monthly = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/ul/li[1]/ul/li[2]/a')
        sidebar_monthly.click()
        driver.implicitly_wait(100)
    month_attend()
    
    #Export excel_daily
    def monthly_export():
        excel_exp = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
        excel_exp.click()
        driver.implicitly_wait(10)
        #export setting & export          
        month_export_download= driver.find_element(by=By.CLASS_NAME, value='btn.btn.btn-outline-primary.fz-md.ml-2.nowrap-hidden')
        month_export_download.click()
        driver.implicitly_wait(100)

        #finish download and close setting window
        close_setting = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/main/div/div/div/div/div/div[4]/div[1]/div/div/footer/button[1]')
        close_setting.click()
        driver.implicitly_wait(100)
    monthly_export()




                                




            

UI_xs()
