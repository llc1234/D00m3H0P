import os
import colorama

colorama.init()

# print(colorama.Fore.GREEN + f"@PR0XY7R41L")

# print(colorama.Fore.GREEN + 'color test')

# print(colorama.Style.RESET_ALL)
# print('back to normal now')


programs = [
    ["TCP_server",     "version 1.0.0"],
    ["TCP_client",     "version 1.0.0"],
    ["rat_maker",      "version 0.7.0"],
    ["backdoor_maker", "version 0.1.0"]
]

while True:
    print("")
    for i in range(len(programs)):
        print(f"{colorama.Fore.GREEN}[{i}]-[{programs[i][0]}] - {programs[i][1]}")
    print("")

    ch = input(colorama.Fore.GREEN + "@PR0XY7R41L=>")

    try:
        if ch.lower() == "clear":
            os.system("cls")
        elif int(ch) > len(programs) - 1:
            print("error")
        else:
            os.system(f"python programs/{programs[int(ch)][0]}.py")

    except:
        print("error")
