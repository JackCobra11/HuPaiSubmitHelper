# Created by COBRA11
# 多按键监听辅助

import pyautogui as auto
import keyboard
import time
from pymouse.windows import PyMouse
import threading

OPERATION_DELAY = 0.2 # 操作延时
SUBMIT_POS = (1170,790) # 默认确认键位置
BID_POS=(1393,625) # 默认出价键位置

class calibration(): # 校正
    def bid(self):
        print("按下 *S* 确认当前鼠标位置为 *出价* 坐标：")
        keyboard.wait('s')  # 等待输入 S
        self.pos_now = PyMouse().position()
        print(self.pos_now)
        time.sleep(OPERATION_DELAY)
        return self.pos_now

    def submit(self):
        print("按下 *Enter* 确认当前鼠标位置为 *确认* 坐标：")
        keyboard.wait('enter')  # 等待输入 ENTER
        self.pos_now = PyMouse().position()
        print(self.pos_now)
        time.sleep(OPERATION_DELAY)
        return self.pos_now


class OperationPart():
    def Bid(self):
        print("Please check the *出价* postion!")
        print(" *出价* 坐标为",BID_POS)

        while True:
            keyboard.wait('s') # 等待输入 S
            auto.click(BID_POS) # 按S后自动点击出价键
            time.sleep(OPERATION_DELAY)

    def Submit(self):
        print("Please check the *确认* postion!")
        print(" *确认* 坐标为",SUBMIT_POS)

        while True:
            keyboard.wait('enter') # 等待输入回车
            auto.click(SUBMIT_POS) # 按回车后自动点击确认键
            time.sleep(OPERATION_DELAY)

if __name__ == "__main__":
    BID_POS = calibration().bid()
    SUBMIT_POS = calibration().submit()
    print("Press *S* to bid the price!")
    print("Press *Enter* to submit the price!")
    t1 = threading.Thread(target=OperationPart.Bid, args=("t1",))
    t2 = threading.Thread(target=OperationPart.Submit, args=("t2",))
    t1.start()
    t2.start()
