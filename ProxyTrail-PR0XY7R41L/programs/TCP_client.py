import os
import time
import socket
import colorama
import threading

colorama.init()

print(colorama.Fore.RED + "\nTCP_Client...\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sett = {
    "ip" : "127.0.0.1",
    "port" : "5050"
}

def start_server(conn):
    is_conn = True

    while is_conn:
        try:
            while True:
                commands = input(colorama.Fore.MAGENTA + f"{sett["ip"]}$>" + colorama.Fore.BLUE)
                if commands.lower() == "exit":
                    is_conn = False
                    break

                conn.send(bytes(commands, "utf-8"))
                conn.settimeout(0.8)

                while True:
                    try:
                        print(conn.recv(16).decode("utf-8"), end="")
                    except socket.timeout:
                        break
        except:
            pass

while True:
    n = input(colorama.Fore.RED + f"@TCP_Client=>").lower().replace("  ", " ").split(" ")

    try:
        if n[0] == "show":
            if n[1] == "options":
                print("")
                for pp in sett:
                    print(f"{pp} = {sett[pp]}")
                print("")

        elif n[0] == "set":
            print("")
            print(f"{n[1]} = {n[2]}")
            print("")

            sett[n[1]] = n[2]

        elif n[0] == "run" or n[0] == "exploit":
            try:
                ip = sett["ip"]
                port = int(sett["port"])
                
                print("waiting for connection...")
                s.connect((ip, port))
                print(f"connection is running. ip:{ip}, port:{port}\n")
                
                start_server(s)

            except:
                print("error")

        elif n[0] == "exit":
            break

    except:
        print("error")

    