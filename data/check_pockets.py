import time
import os

def install_librarys():

    os.system('pip install art')
    print("[SUCCESS] Art kutubxonasi yuklandi.")
    time.sleep(2)
    os.system('pip install pyautogui')
    print("[SUCCESS] Pyautogui kutubxonasi yuklandi.")
    time.sleep(2)
    os.system('pip install subprocess')
    print("[SUCCESS] Subprocess kutubxonasi yuklandi.")
    time.sleep(2)
    os.system('pip install pyspeedtest')
    print("[SUCCESS] Pyspeedtest kutubxonasi yuklandi.")
    time.sleep(2)
    print("[SUCCESS] Speedtest-CLI kutubxonasi yuklandi.")
    os.system('pip install speedtest-cli')


def check_module()-> bool:
    try:
        from art import tprint
        import socket,os,time,random
        import pyautogui
        import subprocess.run
        import speedtest
        return True
    except ImportError:
        return False

if check_module():
    print("[INFO] Kutubxonalar bilan xatolik mavjud emas!")
    with open("info.txt", "w") as f:
        f.write("success")

else:
    print("[ERROR] Ba'zi bir kutubxonalar mavjud emas! O'rnatish funksiyasi ishga tushdi!")
    time.sleep(2)
    install_librarys()
    with open("info.txt", "w") as f:
        f.write("success")



