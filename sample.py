import subprocess
import pyautogui
from time import sleep
from clicknium import clicknium as cc, locator, ui
from clicknium.common.enums import *
from clicknium.common.models.mouselocation import MouseLocation

def main():

    start_process()  


def start_process():
    path = "E:\千牛\AliWorkbench.exe"
    subprocess.Popen(path)  
    print('start_process end.')
    login()
    sleep(5)
    openurl()

def login():

    ui(locator.sample.aliworkbench.login).click()
    print('login end.')

def openurl():
    ui(locator.sample.aliworkbench.setting_in).click() #设置入口
    cc.wait_appear(locator.sample.aliworkbench.setting_menu) #等待设置列表出现
    ui(locator.sample.aliworkbench.setting_button).click() #打开设置

    #ui(locator.sample.aliworkbench.auxiliary).click(MouseButton.Right,modifier_key=("ctrl","shift")) #鼠标事件输入 shift+ctrl+右键
    #ui(locator.sample.aliworkbench.auxiliary).mouse_down(mouse_button="right",by="mouse-emulation",modifier_key="shift") #鼠标按下进行控制 shift+ctrl+右键

    pyautogui.keyDown('shift') 
    pyautogui.keyDown('ctrl')
    ui(locator.sample.aliworkbench.auxiliary).click(MouseButton.Right)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')


if __name__ == "__main__":
    main()
