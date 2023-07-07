import requests
import re
import threading
import os
import time
from colorama import Fore

y = Fore.YELLOW
g = Fore.GREEN

os.system('cls')

print(f'''{Fore.RED}
 _____                                        _____                                 
|  __ \                                      / ____|                                
| |__) |__ _  ___ ___ ___   ___  _ __  ___  | (___   ___ __ _ _ __  _ __   ___ _ __ 
|  _  // _` |/ __/ __/ _ \ / _ \| '_ \/ __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| | \ \ (_| | (_| (_| (_) | (_) | | | \__ \  ____) | (_| (_| | | | | | | |  __/ |   
|_|  \_\__,_|\___\___\___/ \___/|_| |_|___/ |_____/ \___\__,_|_| |_|_| |_|\___|_|   
Made by crxelty''')

def clear():
        print(f'{y}[*] Clearing..')
        with open('servers.txt','w') as i:
            i.write('')
        time.sleep(1)
        print(f'{g}[+] Cleared!')
        time.sleep(1)

        print(f'{y}[*] Close Raccoon Scanner to go back!')
        time.sleep(1)

def find():
        while True:
            url = "https://minecraft-mp.com/servers/random/"
            r = requests.get(url).text
            r = str(re.findall(r'<strong>(.*?)</strong></button>', r))
            r = r.replace('[', '').replace(']', '').replace(',', '\n').replace('\'', '').replace(' ', '')                 
            print(r)

            with open('servers.txt', 'a') as e:
                    if ':25565' in r:
                                r = r.replace(':25565', '')
                                e.write(r)

                    else:
                        with open('servers.txt', 'a') as e:
                                    e.write(r)


threads = []
clear()
for i in range(int(300)):
    t = threading.Thread(target=find)
    t.start()
    threads.append(t)