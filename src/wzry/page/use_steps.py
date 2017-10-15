from name_steps import *
from src.wzry.utils.page_utils import *
import time


def __wait_pic(driver,name,wait_time=5,buffer_time=0.5):
    point=(-1,-1)
    print('used to add:'+str(time.time()))
    end_time=time.time()+float(wait_time)
    print('endtime:'+str(end_time))
    while(time.time()<end_time):
        print('now_start:'+str(time.time()))
        point=get_pic_click_location(driver,name,react_percent=(0.3,0.5,0.5,0.5))
        print(point)
        if point!=(-1,-1):
            end_time=0
            continue
        time.sleep(buffer_time)
        print('now_end:'+str(time.time()))
    if point==(-1,-1):
        raise Exception('wait '+name+' failed! please check')
    return point


def click_start_game_position(driver):
    point= __wait_pic(driver,START_GAME,20)
    driver.tap([point],500)



def click_battle_position():
    return (600,600)

def get_pvp_position():
    return (446,772)

def get_grena():
    return (416,752)
