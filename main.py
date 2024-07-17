from data.ddos import runddos
from data.attack_pc import pc_attack
from data.autowrite import run_sms
from data.check_pockets import check_module

import datetime as dt
import platform
from data.check_connection import test_connection
def menu():
    while True:
        print(r"""
    ___ ___ ___      _____     ___ ____ ___    ______      _____     _____       ____   ___
    |   |   |   |   | ____|   |   |    |   |   |   _ \     |  |\ \   |  ____|    |    | /  /
    |   |   |   |   | |____   |   |    |   |   |  | | \    |  | \ \  |  |        |    |/  /
    |   |___|   |   |____  |  |   |____|   |   |  | |  \   |  | / /  |  _____    |    |  /
    |   |___|   |        | |  |   |____|   |   |  | |  |   |  |/ /   |  _____|   |    |/ \
    |   |   |   |        | |  |   |    |   |   |  |/  /    |  |\ \   |  |        |    |\  \
    |   |   |   |	_____| |  |   |    |   |   |     /     |  | \ \  |  |_____   |    | \  \
    ____    ____   ________|   ___      ____   |____/      |__| /_/  _________|  |____|  \__\
     """)
        x = platform.system()
        print(f"Systema turi {x}")


        x = dt.datetime.now()
        # print(x)
        vaqt = dt.datetime.now()
        yil = x.year
        kun = x.strftime("%A")

        print(f"Hozirgi yil {yil}")
        print(f"Hozirgi soat {vaqt}")

        print("\n****************************************************************")
        print("\n         [1] - DDOS hujum                                       *")
        print("\n         [2] - Internet tezligini o'lchash                      *")
        print("\n         [3] - Do'stlarni lol qoldirish                         *")
        print("\n         [4] - Boshqa kompyuterlarga ulanib boshqarish          *")
        print("\n         [5] - Chiqish                                          *")
        print("\n****************************************************************")

        try:
            ask_menu = input("Menu: ")
            if ask_menu == '1':
                    runddos()
            if ask_menu == '2':
                    pass
            if ask_menu == '3':
                    run_sms()
            if ask_menu == '4':
                    pc_attack()
            if ask_menu == '5':
                print("[STOPPED] Dasturdan chiqildi.")
                break

            else:
                    print("[ERROR] Bunday menu mavjud emas!")

        except KeyboardInterrupt:
            print("[STOPPED] Dasturdan chiqildi.")
try:
    with open("info.txt", "r") as f:
        data = f.readline()
except FileNotFoundError:
    print("[ERROR] INFO fayl mavjud emas!")


if __name__ == '__main__':
    if test_connection():
        if data == 'success':
            menu()
        else:
            check_module()
            menu()
    else:
        print("Internet bilan aloqa mavjud emas❌")