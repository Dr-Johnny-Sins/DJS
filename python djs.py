import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [+] JOIN WHATSAPP GROUP')
os.system('xdg-open https://chat.whatsapp.com/GrMaqHEYlbOJJZzc1h2VVU')
djs=platform.architecture()[0]
if djs=="32bit":
    os.system('clear')
    print('\033[91;1m [+] 32 Bit Device Not Working')
elif djs=="64bit":
    __import__("p64")
