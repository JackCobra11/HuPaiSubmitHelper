import pyautogui as auto
import keyboard
import time
from pymouse.windows import PyMouse

OPERATION_DELAY = 0.2 # 操作延时
submit_pos = (1070,790) # 默认确认键位置

def wait_for_pos():
    print("点击回车确认当前鼠标位置为确认键坐标：")
    keyboard.wait('enter')  # 等待输入回车
    print(PyMouse().position())
    time.sleep(OPERATION_DELAY)

def Submit():
    print("Please check the *Submit_Button* postion!")
    print("x=",x,"y=",y)
    submit_pos = (x, y) # 设置确认键位置
    print("Press *Enter* to submit the price!")
    while True:
        keyboard.wait('enter') # 等待输入回车
        auto.click(submit_pos) # 按回车后自动点击确认键
        time.sleep(OPERATION_DELAY)

if __name__ == "__main__":
    wait_for_pos()
    x, y = PyMouse().position()
    Submit()

