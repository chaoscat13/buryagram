from colorama import Fore
import os
import sys
os.system('cls' if os.name=='nt' else 'clear')
os.system("toilet --width 70 -f pagga -F border --metal 'SCRAPER  '       ")

os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")
os.system("sleep 3")



os.system('cls' if os.name=='nt' else 'clear')


os.system("toilet --width 70 -f pagga -F border --metal 'KABIRA '       ")

from pyrogram import Client
import time
import sys


alf = open("Sessions.txt","r").read()
alf1 = alf.split()

app = Client("Sessions/"+str(alf1[0]),int(alf1[1]),str(alf1[2]),phone_number=str(alf1[3])).start()


class GroupToGroup_Scrap():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app.get_chat(Link1)
            a = self.Group_ChatID.id

    def Scrap(self, Source):
        members = app.iter_chat_members(Source)
        f = open("Members.txt","a")
        counter = 1
        for member in members:
            try:
                user_id = member.user.username
                f.write(str("\n"+user_id))
            except:
                pass
        f.close()

one = input("Source group to scrape member Usernames: ")
print ("Members Scraping Started")
if "@" in str(one):
    onee = one.replace("@","")
else:
    onee = one
app.join_chat(str(onee))
App_Start = GroupToGroup_Scrap()
ab = App_Start.Get_group_chat_id(one)
App_Start.Scrap(a)
app.stop()

print("\n\n Finished !!!!! \n\n")

time.sleep(2)
sys.exit()

