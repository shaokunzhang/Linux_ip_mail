#-*-coding:utf-8-*-
import winput
import time
from winput.vk_codes import *
winput.set_mouse_pos(1057, 344)     #鼠标切换EXCEL
time.sleep(0.5)
winput.click_mouse_button(1)       
def printtime():
    winput.press_key(VK_CONTROL)
    winput.press_key(VK_LSHIFT)
    winput.click_key(VK_OEM_1)
    winput.release_key(VK_CONTROL)
    winput.release_key(VK_LSHIFT)