from src.base import resume_urllib
from PIL import Image
from src.helper.pytesser import pytesser

COLOR_RGB_BLACK = 0


def get_unconglutination_word(img):
    p_x = [0 for _ in xrange(img.size[0])]
    width, height = img.size
    for x in xrange(width):
        for y in xrange(height):
            if img.getpixel((x, y)) == COLOR_RGB_BLACK:
                p_x[x] = 1
                break
    return p_x


def get_location_cut(list):
    location = []
    flag = 0
    start = 0
    for x in range(len(list)):
        if list[x] == 1 and flag == 0:
            start = x
            flag = 1
        elif list[x] == 0 and flag == 1:
            location.append((start, x))
            flag = 0
        elif x == len(list) - 1 and list[x] == 1:
            location.append((start, x))
    return location


def cut_word_with_location(location_list, img):
    xsize, ysize = img.size
    result = ''
    for (a, b) in location_list:
        box = [a - 2, 0, b + 2, ysize]
        region = img.crop(box)
        region.show()
        result += pytesser.image_to_string(region)
        print(result)
    return result.replace('\n', '')


def get_img(img):
    # im=Image.open("E:\\workspase\\ResumeDownloadWithPython\\src\\ValidateCodePicture\\10-1091640.jpg")
    imgry = img.convert('L')
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
    return out

def get_resume(out):
    m_result = ''
    x_range = get_unconglutination_word(out)
    print(x_range)
    location_list = get_location_cut(x_range)
    print(location_list)
    result = cut_word_with_location(location_list, out)
    print(result)
    if result.isalnum() and len(result) == 5:
        m_result = result
    else:
        m_result = pytesser.image_to_string(out)
    print(m_result)
    return m_result
