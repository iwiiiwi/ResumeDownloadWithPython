from src.base import resume_urllib
from PIL import Image
from src.helper.pytesser import pytesser

COLOR_RGB_BLACK=0

def get_unconglutination_word(img):
    p_x=[0 for _ in xrange(img.size[0])]
    width, height =img.size
    for x in xrange(width):
        for y in xrange(height):
            if img.getpixel((x,y))==COLOR_RGB_BLACK:
                p_x[x]=1
                break
    return p_x

def get_location_cut(list):
    location=[]
    flag=0
    start=0
    for x in range(len(list)):
        if list[x]==1 and flag==0:
            start=x
            flag=1
        elif list[x]==0 and flag==1:
            location.append((start,x))
            flag=0
        elif x==len(list)-1 and list[x]==1:
            location.append((start,x))
    return location

# def cut_word_with_location

# picPath=resume_urllib.download_pic()
# im=Image.open(picPath)
im=Image.open("F:\\workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\10-1091258.jpg")
imgry=im.convert('L')
# imgry.show()
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()
x_range=get_unconglutination_word(out)
print("x_range"+x_range)
location_list=get_location_cut(x_range)
print("location_list"+location_list)

# xsize, ysize=out.size
# box=(50,0,xsize,ysize)
# region=out.crop(box)
# region.show()
# print(pytesser.image_to_string(region))
print(pytesser.image_to_string(out))
