COLOR_RGB_BLACK=0

# def get

def get_projection_x(img):
    p_x=[0 for _ in xrange(img.size[0])]
    width, height =img.size

    for x in xrange(width):
        for y in xrange(height):
            print(img.getpixel((x,y)))
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
            if len<22:
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
    return joint_seq

