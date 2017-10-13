from PIL import Image
from find_pic_python_util import *
import datetime

def create_start_button(big_bmp):
    point=(498,560)
    width,height=(280,67)
    create_search_pic(big_bmp,point,width,height)

def show_pic_result(big_bmp,search_bmp):
    t1=datetime.datetime.now()
    points=get_img_points(search_bmp,0.01)
    react_percent=(0.3,0.5,0.3,0.3)
    # react_percent=(0,0,1,1)
    point=find_pic(big_bmp, search_bmp,0.8,points,react_percent)
    print(point)
    t2=datetime.datetime.now()
    print(t2-t1)
    width,height=search_bmp.size
    box=(point[0],point[1],point[0]+width,point[1]+height)
    big_bmp.crop(box).show()



#
big_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\681933661796332341.jpg")
search_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\cut_681933661796332341.jpg")
# big_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\10-11221441login.png")
# search_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\10-11221441code.png")
# search_bmp = Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\cut_10-11221441login.png")
show_pic_result(big_bmp,search_bmp)