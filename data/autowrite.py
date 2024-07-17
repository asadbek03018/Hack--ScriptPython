import pyautogui

def run_sms():
    import pyautogui
    import time
    print("[INFO] Cheksiz so'zlar yozib do'stlaringizni lol qoldiring!")
    try:

        xabar = input("Xabar yozing\n>>")
        nechta = int(input("Necha marta takrorlansin>> "))
        print("[INFO] Tayyorlaning 10 sekund(Telegram, yoki WHatsappga kirib oling. Do'stingizni akkauntini tanlang. Mana sizga cheksiz so'zlar)")

        print("[INFO] Dasturni to'xtatish uchun (CTRL+C)")
        time.sleep(10)

        for i in range(nechta):
            pass
        while nechta > 0:
            nechta -= 1

        pyautogui.typewrite(xabar.strip())
        pyautogui.press('enter')

    except KeyboardInterrupt:
        print("[STOPPED] Dastur to'xtatildi!")
