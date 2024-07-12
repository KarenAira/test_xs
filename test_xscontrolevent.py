# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
import time


service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#download
prefs={"download.default_directory":"\download"}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=service, options=options)
    
driver.get("http://192.168.10.97/")

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


    
def test_xscontrolevent():


    driver.set_window_size(1936, 1056)
    driver.find_element(By.CSS_SELECTOR, ".text-left > .btn").click()
    element = driver.find_element(By.XPATH, "//div/button")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.LINK_TEXT, "門禁").click()
    driver.find_element(By.LINK_TEXT, "門禁管理").click()
    element = driver.find_element(By.LINK_TEXT, "門禁管理")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    driver.find_element(By.XPATH, "//input").click()
    driver.find_element(By.XPATH, "//select").click()
    #driver.find_element(By.CSS_SELECTOR, ".d-block .col-sm-12:nth-child(2) > .row").click()
    #driver.find_element(By.CSS_SELECTOR, ".multiselect__tags").click()
    #driver.find_element(By.CSS_SELECTOR, ".multiselect__tags").click()
    #driver.find_element(By.CSS_SELECTOR, ".d-block .col-sm-12:nth-child(2) > .row").click()
    driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/select").click()
    driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/select").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-primary:nth-child(1)").click()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.CSS_SELECTOR, ".vxe-body--row:nth-child(1) .vxe-switch--button").click()
    driver.find_element(By.CSS_SELECTOR, ".is--off .vxe-switch--icon").click()
    driver.find_element(By.CSS_SELECTOR, ".row--stripe .vxe-switch--icon").click()
    driver.find_element(By.CSS_SELECTOR, ".is--off > .vxe-switch--button").click()
    driver.find_element(By.CSS_SELECTOR, ".vxe-body--row:nth-child(1) .vxe-cell--checkbox").click()
    driver.find_element(By.CSS_SELECTOR, ".is--checked > .vxe-checkbox--checked-icon").click()
    driver.find_element(By.CSS_SELECTOR, ".row--stripe .vxe-checkbox--unchecked-icon").click()
    driver.find_element(By.CSS_SELECTOR, ".is--checked > .vxe-checkbox--checked-icon").click()
    driver.find_element(By.XPATH, "//span/input").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-primary:nth-child(1)").click()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.LINK_TEXT, "門禁裝置設定").click()
    driver.find_element(By.XPATH, "//input").click()
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .btn > div").click()
    element = driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .btn > div")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.XPATH, "//div[3]/div/table/tr[2]/td/div/select").click()
    driver.find_element(By.XPATH, "//div[3]/div/table/tr[2]/td/div/select").click()
    driver.find_element(By.XPATH, "//div[3]/div/table/tr[2]/td/div/select").click()
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) tr:nth-child(2) > .table-td:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".c-switch-slider").click()
    driver.find_element(By.CSS_SELECTOR, ".c-switch-slider").click()
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .btn > div").click()
    element = driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .btn > div")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.LINK_TEXT, "遠端觸發").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    element = driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.LINK_TEXT, "事件").click()
    driver.find_element(By.LINK_TEXT, "事件管理").click()
    
    driver.find_element(By.CSS_SELECTOR, ".vxe-switch--button").click()
    driver.find_element(By.CSS_SELECTOR, ".vxe-switch--icon").click()
    driver.find_element(By.CLASS_NAME, value="btn.btn-outline-primary.btn-in-cell.p-0").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-w-normal").click()
    driver.find_element(By.LINK_TEXT, "看板").click()
    driver.find_element(By.LINK_TEXT, "迎賓看板").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
    element = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .btn").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .btn").click()
    driver.find_element(By.LINK_TEXT, "點名看板").click()
    element = driver.find_element(By.LINK_TEXT, "點名看板")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.LINK_TEXT, "容留看板").click()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.CSS_SELECTOR, ".c-header-nav-link > div").click()
    driver.find_element(By.LINK_TEXT, "登出").click()
  
test_xscontrolevent()