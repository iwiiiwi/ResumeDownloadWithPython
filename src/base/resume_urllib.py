import urllib2
import re
import time
import os

def download_pic():
    response=urllib2.urlopen('http://www.cjol.com/hr/')
    html=response.read()
    # <img id="validatecodePicture_layer" border="0" class="img-hrcode" src="http://newrms.cjol.com/Common/ValidateCodePicture?Key=1&amp;guid=714c2dab-383f-0ee0-be22-be1b8a4d8d51">
    reg=r'http://newrms.cjol.com/Common/ValidateCodePicture.+"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    imgUrl=imglist[0][:-1]
    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))+str(t.__getattribute__("tm_hour"))+str(t.__getattribute__("tm_min"))+str(t.__getattribute__("tm_sec"))
    picpath=os.path.abspath('../ValidateCodePicture')
    if not os.path.exists(picpath):
        os.makedirs(picpath)
    target=picpath+'\\%s.jpg' %foldername
    with open(target,"wb") as file:
        file.write(urllib2.urlopen(imgUrl).read())
    return target

# for x in range(10):
#     download_pic()


# def get_pic():
#     response=urllib2.urlopen('http://www.cjol.com/hr/')
#     html=response.read()
#     # <img id="validatecodePicture_layer" border="0" class="img-hrcode" src="http://newrms.cjol.com/Common/ValidateCodePicture?Key=1&amp;guid=714c2dab-383f-0ee0-be22-be1b8a4d8d51">
#     reg=r'http://newrms.cjol.com/Common/ValidateCodePicture.+"'
#     imgre=re.compile(reg)
#     imglist=re.findall(imgre,html)
#     imgUrl=imglist[0][:-1]
#     urllib2.urlopen(imgUrl).read()