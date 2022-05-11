from __future__ import print_function
import ctypes, sys
import sys
import requests
import os
import platform

hostsfile = "C:\Windows\System32\drivers\etc\hosts"

def welcome():
    print("欢迎使用github加速访问工具，请选择您要运行的功能")
    print("1:加速访问github")
    print("2:关闭加速访问github")
    print("3:退出")
    inp = input("请输入数字键来进行处理:")
    if(inp == "1"):
        changehosts()
    elif(inp == "2"):
        changebackhosts()
    elif(inp == "3"):
        sys.exit()
    else:
        print("未知的指令，请重试");
        welcome()
        


def changehosts():
    os.system('copy '+hostsfile+' '+hostsfile+".bak")
    fp=open(hostsfile,'w')
    gethosts = requests.get("https://cdn.jsdelivr.net/gh/qinyihao/GitHub520@main/hosts");
    if gethosts.status_code == 200:
        print(gethosts.text,file=fp);
        fp.close()
        print("执行完成")

def changebackhosts():
    if(os.path.exists(hostsfile+".bak") == True):
        os.remove(hostsfile)
        os.rename(hostsfile+".bak",hostsfile)
        print("检测到备份文件存在，命令已经成功执行")
    else:
        print("备份文件不存在，不能执行命令，执行失败")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if(platform.system() == "Linux"):
    hostsfile = "/etc/hosts"
    welcome()
elif(platform.system() == "Windows"): 
    if is_admin():
        welcome()
    else:
        print("权限不足，尝试申请权限")
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
else:
    print("未知的系统，程序即将退出")
    sys.exit()



