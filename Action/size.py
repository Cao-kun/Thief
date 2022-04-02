import random
from time import sleep

import pyautogui
import pynput  # 用于模拟鼠标键盘操作

import win32api


def demo_2():
    # mouse = pynput.mouse.Controller()

    """获取缩放后的分辨率"""
    screen_size_wide = win32api.GetSystemMetrics(0)
    screen_size_high = win32api.GetSystemMetrics(1)

    n = random.randint(3, 8)
    for i in range(n):
        x = random.randint(0, screen_size_wide)
        y = random.randint(0, screen_size_high)
        t = random.randint(1, 5)
        print('x坐标为：%s,y坐标为：%s' %(x,y))
        pyautogui.moveTo(x, y, duration=0.10 * t)
        # mouse.position = (x, y)
if __name__ == '__main__':
    # demo_1()
    demo_2()
