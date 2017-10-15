from src.wzry.utils.page_utils import *
from name_steps import *
from use_steps import *

def prepare_steps(driver):
    __prepare_start_game__(driver)
    click_start_game_position(driver)
    __prepare_close_window_normal__(driver)
    __prepare_close_video__(driver)
    __prepare_prepare_friend__(driver)
    __prepare_prepare_team__(driver)

def __prepare_start_game__(driver):
    # point=(574,577)
    # width,height=(138,32)
    point=(749,843)
    width,height=(432,92)
    create_search_pic(driver,point,width,height,START_GAME)

def __prepare_close_window_normal__(driver):
    point=(1608,111)
    width,height=(87,87)
    create_search_pic(driver,point,width,height,CLOSE_WINDOW)

def __prepare_close_video__(driver):
    point=(1785,57)
    width,height=(77,81)
    create_search_pic(driver,point,width,height,CLOSE_VIDIO)

def __prepare_prepare_friend__(driver):
    point=(909,815)
    width,height=(281,108)
    create_search_pic(driver,point,width,height,PREPARE_FRIEND)

def __prepare_prepare_team__(driver):
    point=(816,743)
    width,height=(281,101)
    create_search_pic(driver,point,width,height,PREPARE_TEAM)
