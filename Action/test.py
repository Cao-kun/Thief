import os,time
import pyautogui as pag

import time    #用于记录每一项操作的时间

try:
    while True:
            print("Press Ctrl-C to end")
            x,y = pag.position() #返回鼠标的坐标
            print(x)
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print(posStr)#打印坐标
            time.sleep(0.2)
            os.system('cls')#清楚屏幕
except  KeyboardInterrupt:
    print('end....')