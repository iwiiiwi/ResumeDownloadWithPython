from PIL import Image
from find_pic_python_util import *
import datetime
import os

def create_start_button(big_bmp):
    point=(574,577)
    width,height=(138,32)
    create_search_pic(big_bmp,point,width,height)

def show_pic_result(big_bmp,search_bmp):
    t1=datetime.datetime.now()
    points=get_img_points(search_bmp,0.01)
    react_percent=(0.3,0.5,0.5,0.5)
    # react_percent=(0,0,1,1)
    point=find_pic(big_bmp, search_bmp,0.8,points,react_percent)
    print(point)
    t2=datetime.datetime.now()
    print(t2-t1)
    width,height=search_bmp.size
    box=(point[0],point[1],point[0]+width,point[1]+height)
    big_bmp.crop(box).show()



#
base_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../ValidateCodePicture'))
big_bmp = Image.open(base_path+"/681933661796332341.jpg")
search_bmp = Image.open(base_path+"/cut_681933661796332341.jpg")
# point=(574,577)
# width,height=(138,32)
# box=(point[0],point[1],point[0]+width,point[1]+height)
# cut_img=big_bmp.crop(box)
# picpath=os.path.abspath('../ValidateCodePicture')+'\\'+'cut_big.jpg'
# big_bmp_path=os.path.abspath('../ValidateCodePicture')+'\\'+'change_big.jpg'
# big_bmp.save(big_bmp_path)
# cut_img.save(picpath,quality=100)
# img=Image.open(picpath)
# big_img_change=Image.open(big_bmp_path)
# print_color_pic(big_img_change)
# print_color_pic(img)
# print_color_pic(big_bmp)
# print_color_pic(search_bmp)
# create_start_button(big_bmp)
# big_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\10-11221441login.png")
# search_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\10-11221441code.png")
# search_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\cut_10-11221441login.png")
show_pic_result(big_bmp,search_bmp)