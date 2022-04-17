import pyautogui as auto
import keyboard
import time
from pymouse.windows import PyMouse
import threading

OPERATION_DELAY = 0.15 # 操作延时
SUBMIT_POS = (1170,790) # 默认确认键位置
BID_POS=(1393,625) # 默认出价键位置

class calibration(): # 校正
    def add(self):
        print("按下 *A* 确认当前鼠标位置为 *加价* 坐标：")
        keyboard.wait('a')  # 等待输入 A
        self.pos_now = PyMouse().position()
        print(self.pos_now)
        time.sleep(OPERATION_DELAY)
        return self.pos_now

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

    def input(self):
        print("按下 *i* 确认当前鼠标位置为 *输入验证码区域* 坐标：")
        keyboard.wait('i')  # 等待输入 I
        self.pos_now = PyMouse().position()
        print(self.pos_now)
        time.sleep(OPERATION_DELAY)
        return self.pos_now

class OperationPart():
    def Add(self):
        print("Please check the *出价* postion!")
        print(" *出价* 坐标为",BID_POS)

        while True:
            keyboard.wait('a') # 等待输入 A
            auto.click(ADD_POS) # 自动点击加价键
            time.sleep(OPERATION_DELAY)
            auto.click(BID_POS) # 延时后自动点击出价键
            time.sleep(OPERATION_DELAY)
            auto.click(INPUT_POS) # 在延时后自动点击输入验证码区域
            time.sleep(OPERATION_DELAY)

    def Bid(self):
        print("Please check the *出价* postion!")
        print(" *出价* 坐标为",BID_POS)

        while True:
            keyboard.wait('s') # 等待输入 s
            auto.click(BID_POS) # 延时后自动点击出价键
            time.sleep(OPERATION_DELAY)
            auto.click(INPUT_POS) # 在延时后自动点击输入验证码区域
            time.sleep(OPERATION_DELAY)

    def Submit(self):
        print("Please check the *确认* postion!")
        print(" *确认* 坐标为",SUBMIT_POS)

        while True:
            keyboard.wait('enter') # 等待输入回车
            auto.click(SUBMIT_POS) # 按回车后自动点击确认键
            time.sleep(OPERATION_DELAY)

if __name__ == "__main__":
    ADD_POS = calibration().add()
    BID_POS = calibration().bid()
    INPUT_POS = calibration().input()
    SUBMIT_POS = calibration().submit()
    print("Press *A* to bid the price!")
    # print("Press *I* to Input the price!")
    print("Press *Enter* to submit the price!")
    t1 = threading.Thread(target=OperationPart.Add, args=("t1",))
    t2 = threading.Thread(target=OperationPart.Submit, args=("t2",))
    t3 = threading.Thread(target=OperationPart.Bid, args=("t3",))

    t1.start()
    t2.start()
    t3.start()
