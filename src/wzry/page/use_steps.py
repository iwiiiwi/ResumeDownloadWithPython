from name_steps import *
from src.wzry.utils.page_utils import *
import time
from src.wzry.exception.TimeOutException import *


def __wait_pic__(driver,name,wait_time=5,buffer_time=0.5,react_percent=(0,0,1,1)):
    point=(-1,-1)
    print('used to add:'+str(time.time()))
    end_time=time.time()+float(wait_time)
    print('endtime:'+str(end_time))
    while(time.time()<end_time):
        print('now_start:'+str(time.time()))
        point=get_pic_click_location(driver,name,react_percent=react_percent)
        print(point)
        if point!=(-1,-1):
            end_time=0
            continue
        time.sleep(buffer_time)
        print('now_end:'+str(time.time()))
    if point==(-1,-1):
        raise TimeOutException('wait '+name+' failed! please check')
    return point

def __wait_click_pic_circulation(driver,name,wait_time=120,buffer_time=1):
    point=(-1,-1)
    end_time=time.time()+float(wait_time)
    while(time.time()<end_time):
        try:
            point=__wait_pic__(driver,name)
        except TimeOutException as e:
            pass
        if point!=(-1,-1):
            driver.tap([point],500)
            print('close window clicked')
            time.sleep(buffer_time)



def click_start_game_position(driver):
    time.sleep(15)
    print('start to find start game button')
    react_percent=(0.3,0.5,0.5,0.5)
    point= __wait_pic__(driver,START_GAME,3000,2,react_percent)
    driver.tap([point],500)
    print('start game clicked')

def click_close_window_normal(driver):
    time.sleep(5)
    print('start to find close window button')
    __wait_click_pic_circulation(driver,CLOSE_WINDOW)


def click_battle_position():
    return (600,600)

def get_pvp_position():
    return (446,772)

def get_grena():
    return (416,752)
