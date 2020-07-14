import winput            #键盘鼠标
import sys
import random
import pickle
import pyperclip
from winput.vk_codes import *
import time
def copy():
    winput.press_key(VK_CONTROL)
    time.sleep(0.2)
    winput.click_key(VK_C)
    time.sleep(0.2)
    winput.release_key(VK_CONTROL)
def paste():
    winput.press_key(VK_CONTROL)
    time.sleep(0.2)
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
def printtime():
    winput.press_key(VK_CONTROL)
    winput.press_key(VK_LSHIFT)
    time.sleep(0.1)
    winput.click_key(VK_OEM_1)
    winput.release_key(VK_CONTROL)
    winput.release_key(VK_LSHIFT)
def run(time_min,time_max,num_x,num_y,deal_x,deal_y):
    print("程序开始")
    time.sleep(1)                      #程序开始
    winput.set_mouse_pos(1702, 111)     #鼠标切换EXCEL 
    winput.click_mouse_button(1)       
    time.sleep(0.5)
    while 1 :                      
        copy()                         #复制
        Random_time=random.randint(time_min,time_max)           
        winput.set_mouse_pos(num_x,num_y)  #鼠标选择ak数量
        winput.click_mouse_button(1)
        time.sleep(0.5)
        ctrl_a()                       #全选
        time.sleep(0.5)
        winput.click_key(VK_DELETE)    #删除
        time.sleep(0.5)
        paste()                        #粘贴
        time.sleep(0.5)
        winput.set_mouse_pos(deal_x,deal_y)  #鼠标点击交易
        winput.click_mouse_button(1)
        time.sleep(1)
        winput.set_mouse_pos(1702, 111) #切换窗口
        winput.click_mouse_button(1)
        time.sleep(0.5)
        winput.click_key(VK_RIGHT)
        printtime()     
        winput.click_key(VK_LEFT)      #左键
        winput.click_key(VK_DOWN)      #下键
        time.sleep(Random_time)   
def cs():
    print("请键入随机时间下限")
    timemin=input()
    if timemin=="":
        time_min=10
    else:
        time_min=int(timemin)
    print("请键入随机时间上限")
    timemax=input()
    if timemax=="":
        time_max=20
    else:
        time_max=int(timemax)
    print("请键入数量坐标X")
    numx=input()
    if numx=="":
        num_x=698
    else:
        num_x=int(numx)
    print("请键入数量坐标Y")
    numy=input()
    if numy=="":
        num_y=698
    else:
        num_y=int(numy)
    print("请键入成交坐标X")
    dealx=input()
    if dealx=="":
        deal_x=794
    else:
        deal_x=int(dealx)
    print("请键入成交坐标Y")
    dealy=input()
    if dealy=="":
        deal_y=794
    else:
        deal_y=int(dealy) 
    aa=[time_min,time_max,num_x,num_y,deal_x,deal_y]
    f=open("var.txt","wb")
    pickle.dump(aa,f,0)
    f.close()
    yx()
def yx():    
    print("请选择\n","1:开始程序  2:参数调整")
    a = int(input())
    if  a==1:
        f=open("var.txt","rb")
        bb=pickle.load(f)
        print(bb)
        run(bb[0],bb[1],bb[2],bb[3],bb[4],bb[5])
    elif a==2:
        cs()
yx()    
            
