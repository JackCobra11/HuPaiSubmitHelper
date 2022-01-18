# 沪牌回车键报价确认助手

## Requirements
PyAutoGUI\
keyboard\
PyMouse\
pymouse_pyhook3

## 操作方法

#### 步骤1
点击回车获取确认键坐标
#### 步骤2
获取坐标后，按提示输入x坐标和y坐标
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
