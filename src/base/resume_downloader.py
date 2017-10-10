from selenium import webdriver
from resume_urllib import *
import os
from src.helper.image_helper import *

path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../resource/chromedriver/chromedriver_2.32_32bit_win.exe'))
driver=webdriver.Chrome(path,0,None,None,None,None)
# driver.get("http://www.cjol.com/")
# driver.find_element_by_xpath("//a[@href='http://www.cjol.com/hr']").click()
# http://www.cjol.com/hr/
driver.get("http://www.cjol.com/hr/")
driver.find_element_by_id('LoginName').send_keys('yidatecERP')
driver.find_element_by_id('LoginPassword').send_keys('yidatec20170801')
url=driver.find_element_by_id('validatecodePicture_layer').get_attribute('src')
path=download_pic(url)
img=Image.open(path)
out=get_img(img)
result=get_resume(out)
driver.find_element_by_id('ValidateCode').send_keys(result)
driver.find_element_by_id('btnLogin').click()
# while True:
#     str=input("input:")
#     if(str=='quit'):
#         driver.quit()
#         break