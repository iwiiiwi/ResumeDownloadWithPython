from PIL import Image
from find_pic_python_util import *

big_bmp = Image.open("E:\\Workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\10-11221441login.png")
# big_bmp.show()
search_bmp = Image.open("E:\\Workspase\\ResumeDownloadWithPython\\src\ValidateCodePicture\\10-11221441code.png")
# search_bmp.show()
points=get_img_points(search_bmp,0.001)
point=find_pic(big_bmp, search_bmp,0.8,points)

print(point)
