import time

OPERATION_DELAY = 0.15 # 操作延时

ADD_POS = (1405,480) # 默认加价键位置
SUBMIT_POS = (1151,742) # 默认确认键位置
BID_POS = (1406,596) # 默认出价键位置
INPUT_POS = (1280,648) # 默认输入验证码区域


SUBMIT_TIME = "2022-4-18 21:44:10"
SUBMIT_TIMESTAMP = int(time.mktime(time.strptime(SUBMIT_TIME, "%Y-%m-%d %H:%M:%S")))
print(SUBMIT_TIMESTAMP-time.time())