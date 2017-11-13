from pymouse import PyMouse
from pykeyboard import PyKeyboard

k=PyKeyboard();

def move_up():
    k.press_keys('w','d')