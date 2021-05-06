from colorama import Fore
import os
import sys
os.system('cls' if os.name=='nt' else 'clear')

os.system("toilet --width 70 -f pagga -F border --metal 'ADDER  '       ")

os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")
os.system("sleep 3")



os.system('cls' if os.name=='nt' else 'clear')

os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")

from pyrogram import Client
import time
import sys

alf = open("Sessions.txt","r").read()
alf1 = alf.split()

i = 1
j = 0

while True:
    try:
        a = str(alf1[j])
        b = int(alf1[j+1])
        c = str(alf1[j+2])
        d = str(alf1[j+3])
    except:
        print("Finished")
        sys.exit()
    app = Client("Sessions/"+a,b,c,phone_number=d)
    app.start()
    app.send_message("me",str(i))
    app.stop()
    print("Session "+str(i)+" Created !")
    i += 1
    j += 4

time.sleep(2)
sys.exit()

