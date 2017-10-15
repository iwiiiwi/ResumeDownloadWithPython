from appium import webdriver
from page.prepare_steps import *
from page.use_steps import *

def start_wzry_driver():
    desired_caps={}
    desired_caps['deviceName']='df836a957d73'
    desired_caps['platformName'] = 'Android'
    desired_caps['androidPackage'] = 'com.tencent.tmgp.sgame'
    desired_caps['appActivity'] = '.SGameActivity'
    desired_caps['newCommandTimeout']='600'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



try:
    driver=start_wzry_driver()
    print('start to wait')
    time.sleep(20)
    print('start to find pic')
    point=click_start_game_position(driver)
    # prepare_steps(driver)

    print('hhhh')
finally:
    driver.quit()