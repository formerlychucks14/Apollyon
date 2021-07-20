import amino
import pyfiglet
import colorama
from colorama import Fore, Back, Style
import threading 

print(Fore.BLUE)
print(Style.BRIGHT)

Introduction = pyfiglet.figlet_format("Apollyon", font="colossal")
print(Introduction)
print("Script made by Sneed. Have fun (:")

email = input("Bot Email: ")
password = input("Bot Password: ")

client = amino.Client()
client.login(email=email, password=password)
print("Logged in the bot account successfully.")

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id)

comId = input("Community ID: ")
sub_client = amino.SubClient(comId=comId, profile=client.profile)
print("Accessed the Community.")

title = input("Wiki Title: ")
content = input("Wiki Content: ")

def WikiSpammer():
    while True:
     try:
        sub_client.post_wiki(title=title, content=content)
     finally:
         pass
         print("The community is being trolled. Good luck.")

threads = []

for i in range(50):
    t = threading.Thread(target=WikiSpammer)
    t.daemon = False
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()






