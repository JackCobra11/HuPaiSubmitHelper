# 沪牌拍卖出价助手


## 2022.4.17 更新 Releases
打包为exe\
可直接下载运行[V1.0版本](https://github.com/JackCobra11/HuPaiSubmitHelper/releases/download/%E6%B2%AA%E7%89%8C%E6%8B%8D%E5%8D%96%E5%87%BA%E4%BB%B7%E5%8A%A9%E6%89%8B/V1.0.exe)

## 2022.4.23 更新 拍中实例
<div align="center">
<img src=IMG_20220423_125803.jpg width=60%/>
</div>

预祝大家早日拍上沪牌\
enter_submit.py 单按键辅助\
BidHelper.py 多按键辅助

## Requirements
PyAutoGUI\
keyboard\
PyMouse\
pymouse_pyhook3

## 操作方法

#### 步骤1
将鼠标指针移至确认键位置，按回车获取确认键坐标
#### 步骤2
获取坐标后，确认x坐标和y坐标
#### 步骤3
在输好验证码后，按回车即可确定报价


## 已知问题
在Python3.9之后的版本中，PyMouse可能无法正常工作
### 错误信息1
```doctest
File "X:\python\lib\site-packages\pymouse\__init__.py", line 92, in <module>
    from windows import PyMouse, PyMouseEvent
ModuleNotFoundError: No module named 'windows'
```
#### 修改方法
```doctest
跳转到"X:\python\lib\site-packages\pymouse\__init__.py"
将 line 92 修改为 from pymouse.windows import PyMouse, PyMouseEvent
```
### 错误信息2
```doctest
Traceback (most recent call last):
  File "X:\python\lib\site-packages\pymouse\__init__.py", line 92, in <module>
    from windows import PyMouse, PyMouseEvent
  File "X:\python\lib\site-packages\pymouse\windows.py", line 23, in <module>
    import pythoncom, pyHook
ModuleNotFoundError: No module named 'pyHook'
```
#### 修改方法
```doctest
将 line 22： import pythoncom, pyHook
修改为       import pythoncom
            import pymouse_pyhook3 as pyHook
```


## Stargazers over time

[![Stargazers over time](https://starchart.cc/JackCobra11/HuPaiSubmitHelper.svg)](https://starchart.cc/JackCobra11/HuPaiSubmitHelper)
