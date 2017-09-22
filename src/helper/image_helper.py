from PIL import Image
from src.helper.pytesser import pytesser
from verification_code_helper import *


im=Image.open('ValidateCodePicture1.jpg')
# im=Image.open('number.jpg')
# im=Image.open('wordAndNumber.jpg')
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
get_projection_x=get_projection_x(out)
joint_seq=get_joint_img(get_projection_x)
# box=out.copy()
xsize, ysize=out.size
box=(joint_seq[0],0,joint_seq[1],ysize)
region=out.crop(box)
region.show()
# out.paste(region,box)
out.show()
print(pytesser.image_file_to_string('ValidateCodePicture2.jpg'))
# print(pytesser.image_file_to_string('number.jpg'))
# print(pytesser.image_file_to_string('wordAndNumber.jpg'))
print(pytesser.image_to_string(out))