from selenium import webdriver
from resume_urllib import *
import os
from src.helper.image_helper import *

path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../resource/chromedriver/chromedriver_2.32_32bit_win.exe'))
driver=webdriver.Chrome(path,0,None,None,None,None)
# # driver.get("http://www.cjol.com/")
# # driver.find_element_by_xpath("//a[@href='http://www.cjol.com/hr']").click()
# # http://www.cjol.com/hr/
driver.get("http://www.cjol.com/hr/")
# # driver.find_element_by_id('LoginName').send_keys('yidatecERP')
# driver.find_element_by_id('LoginName').send_keys('dsdfsdf')
# # driver.find_element_by_id('LoginPassword').send_keys('yidatec20170801')
# driver.find_element_by_id('LoginPassword').send_keys('fewfsdfsd')
# t = time.localtime(time.time())
# foldername = str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))+str(t.__getattribute__("tm_hour"))+str(t.__getattribute__("tm_min"))+str(t.__getattribute__("tm_sec"))
# picpath=os.path.abspath('../ValidateCodePicture')
# code_element=driver.find_element_by_id('validatecodePicture_layer')
# driver.maximize_window()
# driver.save_screenshot(picpath+"\\"+foldername+"login.png")
# imgSize=code_element.size
# imgLocation =code_element.location
# rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))
# login = Image.open(picpath+"\\"+foldername+"login.png")
# frame4=login.crop(rangle)
# frame4.save(picpath+"\\"+foldername+"code.png")
# # url=driver.find_element_by_id('validatecodePicture_layer').get_attribute('src')
# # path=download_pic(url)
# img=Image.open(picpath+"\\"+foldername+"code.png")
# out=get_img(img)
# result=get_resume(out)
# driver.find_element_by_id('ValidateCode').send_keys(result)
# driver.quit()
# driver.find_element_by_id('btnLogin').click()
while True:
    print('enter go to continue')
    str=input("input:")
    if(str=='go'):
        # driver.quit()
        print('hahahahhahqui')
        break