from src.wzry.utils.find_pic_python_util import *
from PIL import Image

base_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../res'))
big_bmp = Image.open(base_path+"/screenshot.png")
search_bmp = Image.open(base_path+"/start_game.png")
points=get_img_points(search_bmp,0.01)
point=find_pic(big_bmp,search_bmp,0.8,points,(0.3,0.5,0.5,0.5))
print(point)