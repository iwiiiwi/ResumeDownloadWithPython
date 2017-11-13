import os
from PIL import Image
from find_pic_python_util import *

PIC_PATH=os.path.abspath('./res')+'/'
PIC_TYPE='.png'
SCREENSHOT_PATH=PIC_PATH+'screenshot'+PIC_TYPE
POINT_NUMBER=100

def take_screenshot(driver):
    driver.save_screenshot(SCREENSHOT_PATH)

def __get_screenshot_img__(driver):
    take_screenshot(driver)
    return Image.open(SCREENSHOT_PATH)

def create_search_pic(driver,point,width,height,name):
    screenshot_img=__get_screenshot_img__(driver)
    __save_search_pic__(screenshot_img,point,width,height,name)

def __save_search_pic__(big_img,point,width,height,name):
    box=(point[0],point[1],point[0]+width,point[1]+height)
    cut_img=big_img.crop(box)
    picpath=PIC_PATH+name+PIC_TYPE
    cut_img.save(picpath,'png')

def __get_search_pic__(name):
    picpath=PIC_PATH+name+PIC_TYPE
    return Image.open(picpath)

def get_pic_click_location(driver,name,percent=0.8,react_percent=(0,0,1,1)):
    img=__get_screenshot_img__(driver)
    search_img=__get_search_pic__(name)
    width,heighth=search_img.size
    check_number_percent=1
    if width*heighth>POINT_NUMBER:
        check_number_percent=float(POINT_NUMBER/check_number_percent)
    points=get_img_points(search_img,check_number_percent)
    x,y= find_pic(img,search_img,percent,points,react_percent)
    if x==-1 or y==-1:
        return (-1,-1)
    return (x+int(width/2),y+int(heighth/2))


