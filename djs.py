import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [\033[92;1m+\033[97;1m]\033[97;1m 𝐉𝐨𝐢𝐧 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐆𝐫𝐨𝐮𝐩')
os.system('xdg-open https://chat.whatsapp.com/GrMaqHEYlbOJJZzc1h2VVU')
djs=platform.architecture()[0]
if djs=="32bit":
    os.system('clear')
    print('\033[97;1m [\033[92;1m+\033[97;1m]\033[91;1m 32 Bit Device Not Working')
elif djs=="64bit":
    __import__("djs")
