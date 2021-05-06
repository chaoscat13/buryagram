from colorama import Fore
import os
import sys
os.system('cls' if os.name=='nt' else 'clear')
os.system("toilet --width 70 -f pagga -F border --metal 'ADDER  '       ")

os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")
os.system("sleep 3")



os.system('cls' if os.name=='nt' else 'clear')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")


from pyrogram import Client
import time
import sys
from telethon.sync import TelegramClient
from telethon import types, utils, errors
from telethon.tl.functions import channels, contacts
print(color.BOLD + "\033[1;31;40m1.D\033[1;30;40mo \033[1;32;40mYou Want To Add Member With Your Specific Group")
print ("2.\033[1;31;40mD\033[1;30;40mo \033[1;32;40mYou Want To Add Your Scraped Member ")

orginally = int(input(color.BOLD + "\033[91mT\033[95my\033[36mpe\033[91m number 1 or 2: "))
print (Fore.GREEN + "")
alf = open("Sessions.txt","r").read()
alf1 = alf.split()
lena = len(alf1)
threads = int(lena/4)

app0 = Client("Sessions/"+str(alf1[0]),int(alf1[1]),str(alf1[2]),phone_number=str(alf1[3]))
app1 = Client("Sessions/"+str(alf1[4]),int(alf1[5]),str(alf1[6]),phone_number=str(alf1[7]))
app2 = Client("Sessions/"+str(alf1[8]),int(alf1[9]),str(alf1[10]),phone_number=str(alf1[11]))
app3 = Client("Sessions/"+str(alf1[12]),int(alf1[13]), (alf1[14]),phone_number=str(alf1[15]))
app4 = Client("Sessions/"+str(alf1[16]),int(alf1[17]),str(alf1[18]),phone_number=str(alf1[19]))
#app5 = Client("Sessions/"+str(alf1[20]),int(alf1[21]),str(alf1[22]),phone_number=str(alf1[23]))
#app6 = Client("Sessions/"+str(alf1[24]),int(alf1[25]),str(alf1[26]),phone_number=str(alf1[27]))
#app7 = Client("Sessions/"+str(alf1[28]),int(alf1[29]),str(alf1[30]),phone_number=str(alf1[31]))
#app8 = Client("Sessions/"+str(alf1[32]),int(alf1[33]),str(alf1[34]),phone_number=str(alf1[35]))
#app9 = Client("Sessions/"+str(alf1[36]),int(alf1[37]),str(alf1[38]),phone_number=str(alf1[39]))
#app10 = Client("Sessions/"+str(alf1[40]),int(alf1[41]),str(alf1[42]),phone_number=str(alf1[43]))
#app11 = Client("Sessions/"+str(alf1[44]),int(alf1[45]),str(alf1[46]),phone_number=str(alf1[47]))
#app12 = Client("Sessions/"+str(alf1[48]),int(alf1[49]),str(alf1[50]),phone_number=str(alf1[51]))
#app13 = Client("Sessions/"+str(alf1[52]),int(alf1[53]),str(alf1[54]),phone_number=str(alf1[55]))
#app14 = Client("Sessions/"+str(alf1[56]),int(alf1[57]),str(alf1[58]),phone_number=str(alf1[59]))
#app15 = Client("Sessions/"+str(alf1[60]),int(alf1[61]),str(alf1[62]),phone_number=str(alf1[63]))
#app16 = Client("Sessions/"+str(alf1[64]),int(alf1[65]),str(alf1[66]),phone_number=str(alf1[67]))
#app17 = Client("Sessions/"+str(alf1[68]),int(alf1[69]),str(alf1[70]),phone_number=str(alf1[71]))
#app18 = Client("Sessions/"+str(alf1[72]),int(alf1[73]),str(alf1[74]),phone_number=str(alf1[75]))
#app19 = Client("Sessions/"+str(alf1[76]),int(alf1[77]),str(alf1[78]),phone_number=str(alf1[79]))

apps = [app0, app1, app2, app3, app4]

for app in apps:
    app.start()

aaaaaa = len(apps)

class GroupToGroup_AddMember():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1, Link2):
            global a,b
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id
            self.Group_ChatID = app0.get_chat(Link2)
            b = self.Group_ChatID.id

    def Add_To_Group(self, Source, Destination):
        members = app0.iter_chat_members(Source)
        counter = 1
        ccc = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            try:
                user_id = member.user.username
                app.add_chat_members(Destination, user_id)
            except:
                pass
            else:
                print(" " +str(counter)+"User"+str(user_id))
                
                counter = counter+1
            if ccc == aaaaaa:
                ccc = 1

class GroupToGroup_AddMember1():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        counter = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            ccc = 1
            try:
                app.add_chat_members(Destination, member)
            except:
                pass
            else:
                print(Fore.BLUE + " " +str(counter)+" User Added "+str(member))
                counter = counter+1
            if ccc == aaaaaa:
                ccc = 1
if int(orginally) == 1:
    one = input("Source group: ")
    two = input("Destination group: ")

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@","")
    else:
        twoo = two
    for app in apps:
        app.join_chat(str(onee))
        app.join_chat(str(twoo))

    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(one, two)
    App_Start.Add_To_Group(a, b)

elif int(orginally) == 2:
    one = input("Destination group: ")
    

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    for app in apps:
        app.join_chat(str(onee))

    members = open("Members.txt" , "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember1()
    ab = App_Start.Get_group_chat_id(one)
    App_Start.Add_To_Group(a)

for app in apps:
    app.stop()
    print ("Members Added Successfully")
sys.exit()

