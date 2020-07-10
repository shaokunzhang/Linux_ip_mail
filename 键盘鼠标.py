import winput            #键盘鼠标
from winput.vk_codes import *
import time
def copy():
    winput.press_key(VK_CONTROL)
    winput.click_key(VK_C)
    winput.release_key(VK_CONTROL)
def paste():
    winput.press_key(VK_CONTROL)
    winput.click_key(VK_V)
    winput.release_key(VK_CONTROL)
def tab():
    winput.press_key(VK_MENU)
    winput.click_key(VK_TAB)
    winput.release_key(VK_MENU)
def tab_b():
    winput.press_key(VK_MENU)
    winput.click_key(VK_TAB)
    time.sleep(0.5)
    winput.click_key(VK_TAB)
    winput.release_key(VK_MENU)
def ctrl_a():
    winput.press_key(VK_CONTROL)
    winput.click_key(VK_A)
    winput.release_key(VK_CONTROL)

time.sleep(1)
winput.set_mouse_pos(1307, 235)
winput.click_mouse_button(1)
time.sleep(0.5)
while 1 :
    copy()
    time.sleep(0.5)
    winput.set_mouse_pos(693,260)
    winput.click_mouse_button(1)
    time.sleep(0.5)
    ctrl_a()
    time.sleep(0.5)
    winput.click_key(VK_DELETE)
    time.sleep(0.5)
    paste()
    time.sleep(0.5)
    winput.set_mouse_pos(693,377)
    winput.click_mouse_button(1)
    time.sleep(1)
    winput.set_mouse_pos(520,514)
    winput.click_mouse_button(1)
    time.sleep(0.3)
    winput.click_mouse_button(1)
    copy()
    time.sleep(0.5)
    tab()
    time.sleep(0.5)
    winput.click_key(VK_LEFT)
    time.sleep(0.5)
    paste()
    time.sleep(0.5)
    winput.click_key(VK_RIGHT)
    time.sleep(0.5)
    winput.click_key(VK_DOWN)
    time.sleep(0.5)

     
            
        





































# def if __name__ == "__main__":
#     pass
# time.sleep(0.5)
# winput.set_mouse_pos(833,75)
# time.sleep(0.5)
# winput.click_mouse_button(1)
# winput.set_mouse_pos(983,524)
# time.sleep(0.5)
# winput.click_mouse_button(1)
# open the RUN menu (WIN + R)
# winput.press_key(VK_LWIN)
# winput.click_key(VK_R)
# winput.release_key(VK_LWIN)
# def slow_click(vk_code): # delay each keypress by 1/10 of a second
#     time.sleep(0.1)
#     winput.click_key(vk_code)
# enter "notepad.exe"
# slow_click(VK_N)
# slow_click(VK_O)
# slow_click(VK_T)
# slow_click(VK_E)
# slow_click(VK_P)
# slow_click(VK_A)
# slow_click(VK_D)
# slow_click(VK_OEM_PERIOD)
# slow_click(VK_E)
# slow_click(VK_X)
# slow_click(VK_E)
# slow_click(VK_RETURN)
# time.sleep(1)
# enter "hello world"
# slow_click(VK_H)
# slow_click(VK_E)
# slow_click(VK_L)
# slow_click(VK_L)
# slow_click(VK_O)
# slow_click(VK_SPACE)
# slow_click(VK_W)
# slow_click(VK_O)
# slow_click(VK_R)
# slow_click(VK_L)
# slow_click(VK_D)