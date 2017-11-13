from appium import webdriver
from page.prepare_steps import *
from page.use_steps import *
from src.wzry.utils.page_utils import *

def start_wzry_driver():
    desired_caps={}
    # desired_caps['deviceName']='df836a957d73'
    desired_caps['deviceName']='127.0.0.1:21503 device'
    desired_caps['platformName'] = 'Android'
    desired_caps['appPackage'] = 'com.tencent.tmgp.sgame'
    desired_caps['appActivity'] = '.SGameActivity'
    desired_caps['newCommandTimeout']='600'
    desired_caps['noReset']='true'
    desired_caps['dontStopAppOnReset']='true'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




driver=start_wzry_driver()
try:
    print('start to wait')
    print('start to find pic')
    # click_start_game_position(driver)
    # click_close_window_normal(driver)
    # prepare_steps(driver)

    print('hhhh')
finally:
    driver.quit()