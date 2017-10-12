import random


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
        print(float(count) / float(len(points)))
        if float(count) / float(len(points)) >= percent:
            result = True
    return result


def __eql_img__(big_img, small_img, percent, center_point, points):
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

    for j in xrange(max_x):
        for k in xrange(max_y):
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


def find_pic(big_img, serch_bmp, percent, points):
    center_points = get_img_points(serch_bmp, 5)
    for i in xrange(len(center_points)):
        center_point = center_points[i]
        point=__eql_img__(big_img, serch_bmp, percent, center_point, points);
        if point!=(-1,-1):
            print('find out')
            break
    return point
