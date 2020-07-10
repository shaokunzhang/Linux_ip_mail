import winput            #键盘鼠标
import sys
import random
import threading
import pyperclip
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
def keyboard_callback( event ):
    if event.vkCode == winput.VK_ESCAPE: # quit on pressing escape
        winput.stop()
        sys.exit()
def run():
    print("程序开始")
    time.sleep(1)                      #程序开始
    winput.set_mouse_pos(1722, 20)     #鼠标切换EXCEL 
    winput.click_mouse_button(1)       
    time.sleep(0.5)
    while 1 :                      
        copy()                         #复制
        Random_time=random.randint(60,100)           
        winput.set_mouse_pos(692,698)  #鼠标选择ak数量
        winput.click_mouse_button(1)
        time.sleep(0.5)
        ctrl_a()                       #全选
        time.sleep(0.5)
        winput.click_key(VK_DELETE)    #删除
        time.sleep(0.5)
        paste()                        #粘贴
        time.sleep(0.5)
        winput.set_mouse_pos(733,794)  #鼠标点击交易
        winput.click_mouse_button(1)
        time.sleep(1)
        winput.set_mouse_pos(1726, 20) #切换窗口
        winput.click_mouse_button(1)
        time.sleep(0.5)
        winput.click_key(VK_RIGHT)
        pyperclip.copy(Random_time)
        paste()       
        winput.click_key(VK_LEFT)      #左键
        winput.click_key(VK_DOWN)      #下键
        time.sleep(Random_time)           
def key():
    winput.hook_keyboard( keyboard_callback )
    winput.wait_messages()
    winput.unhook_keyboard()
r=threading.Thread(target=run)
k=threading.Thread(target=key)
r.start()