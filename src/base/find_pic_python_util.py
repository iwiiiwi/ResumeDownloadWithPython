import random
import os


def get_img_points(img, percent):
    width, height = img.size
    count = 1
    if percent > 1:
        count = int(percent)
    else:
        count = int(width * height * percent)
    random.seed()
    points = []
    for i in xrange(count):
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        points.append((x, y))
    return points


def __eql_color__(big_img, center_point, get_center_point, points, points_colors, percent):
    result = False
    count = 0
    big_img_width, big_img_height = big_img.size
    center_point_x, center_point_y = center_point
    get_center_point_x, get_center_point_y = get_center_point
    for i in xrange(len(points)):
        test_point_x, test_point_y = points[i]
        test_point_x = test_point_x - center_point_x + get_center_point_x
        test_point_y = test_point_y - center_point_y + get_center_point_y

        if test_point_x < 0 or test_point_y < 0 or test_point_x >= big_img_width or test_point_y >= big_img_height:
            print('break')
            break
        big_color = big_img.getpixel((test_point_x, test_point_y))
        small_color = points_colors[i]

        if big_color == small_color:
            count+=1
        p=float(count) / float(len(points))
        if p>0.1:
            print(p)
        if float(count) / float(len(points)) >= percent:
            result = True
    return result


def __eql_img__(big_img, small_img, percent, center_point, points,react_percent):
    result = False
    point=(-1,-1)
    x = 0
    y = 0
    max_x, max_y = big_img.size
    center_point_x, center_point_y = center_point
    center_point_color = small_img.getpixel((center_point_x, center_point_y))
    points_colors = []
    for i in xrange(len(points)):
        p_x, p_y = points[i]
        color=small_img.getpixel((p_x, p_y))
        points_colors.append(color)

    if react_percent is None:
        react_percent=(0,0,1,1)
    x,y,w,h=react_percent
    for j in xrange(int(max_x*x),int(max_x*(x+w))):
        for k in xrange(int(max_y*y),int(max_y*(y+h))):
            get_center_point = (j, k)
            get_center_point_color = big_img.getpixel((j, k))
            if center_point_color == get_center_point_color:
                if __eql_color__(big_img, center_point, get_center_point, points, points_colors, percent):
                    result = True
                    point = (j - center_point_x, k - center_point_y)
                    break

        if result == True:
            break
    return point

def print_color_pic(img):
    name=img.filename[img.filename.rfind('\\')+1:len(img.filename)][0:img.filename[img.filename.rfind('\\')+1:len(img.filename)].rfind('.')]+".text"
    picpath=os.path.abspath('../ValidateCodePicture')+'/'+name
    x,y=img.size
    colors=[]
    for i in xrange(x):
        for j in xrange(y):
            color=img.getpixel((i,j))
            colors.append(color)
    with open(picpath,"wb") as file:
        file.writelines(str(colors))




def create_search_pic(big_img,point,width,height):
    box=(point[0],point[1],point[0]+width,point[1]+height)
    cut_img=big_img.crop(box)
    name="cut_"+big_img.filename[big_img.filename.rfind('\\')+1:len(big_img.filename)]
    picpath=os.path.abspath('../ValidateCodePicture')+'/'+name
    cut_img.save(picpath,'JPEG')

def find_pic(big_img, search_bmp, percent, points,react_percent):
    center_points = get_img_points(search_bmp, 5)
    for i in xrange(len(center_points)):
        center_point = center_points[i]
        point=__eql_img__(big_img, search_bmp, percent, center_point, points,react_percent);
        if point!=(-1,-1):
            print('find out')
            break
    return point
