COLOR_RGB_BLACK=0

def get_word_size_x(img):
    size_x=[0,0]
    projection=get_projection_x(img);
    for x in range(len(projection)):
        if projection[x]==1:
            size_x[1]=x
            if size_x[0]==0:
                size_x[0]=x
    return size_x

def get_cut_location(img):
    p_x=[]
    width, height =img.size
    start=0
    end=0
    for x in xrange(width):
        for y in xrange(height):
            if img.getpixel((x,y))==COLOR_RGB_BLACK:
                if start==0:
                    start=x
                    break
            else:
                if start>0:
                    end=x
                    p_x.append((start,end))
                    start=0
                    end=0
                    break

    return p_x

def cut_single_word(img):
    size=get_word_size_x(img);
    single_lengh=(size[1]+1)/5
    start_x=size[0]
    xsize, ysize=img.size
    for x in range(5):
        if x<4:
            box=(start_x+single_lengh*x,0,start_x+5+single_lengh*(x+1),ysize)
        else:
            box=(start_x+single_lengh*x,0,xsize,ysize)
        word=img.crop(box)
        word.show()


def get_projection_x(img):
    p_x=[0 for _ in xrange(img.size[0])]
    width, height =img.size
    for x in xrange(width):
        for y in xrange(height):
            if img.getpixel((x,y))==COLOR_RGB_BLACK:
                p_x[x]=1
                break
    return p_x

def get_joint_img(projection_x):
    joint_seq=[]
    len=0
    joint=0
    end_x=0
    for idx, val in enumerate(projection_x):
        if val==0 and joint ==0:
            continue
        elif val==0 and joint ==1:
            if len<23:
                print(len)
                len=0
                joint=0
                pos_x=0
            else:
                end_x=idx
                break
        elif val==1:
            if joint==0:
                joint=1
                pos_x=idx
            len+=1
    joint_seq=[pos_x,end_x]
    print(len)
    return joint_seq

