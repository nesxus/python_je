"""
------------------
Project_Name:pythonProject
------------------
File Name:  serial_v1
Author :    nexus
date:       2021/7/22
------------------
串口输入测试
"""
import datetime
import re
import serial  # 导入模块
import time

com = "4"  # 端口号
bps = 9600  # 波特率
timex = None


def serial_input(com, bps, timex):
    try:
        ser = serial.Serial("COM" + com, bps, timeout=timex)  # 串口配置：端口，波特率，
        while True:
            if ser.in_waiting:
                str_a = ser.read(ser.in_waiting).hex().upper()
                str_list = re.findall(".{2}", str_a)  # 两个字节分隔
                new_str = " ".join(str_list)
                return new_str

        ser.close()  # 关闭串口
    except Exception as e:
        print("---异常---：", e)

def serial_cmd ():
    serial_cmda = new_str[6:8]
    return serial_cmda

while(1):
    new_str = serial_input(com, bps, timex)
    print(new_str)
    cmda = serial_cmd()
    print(cmda)