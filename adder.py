from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.sync import TelegramClient
import os
import glob
from time import sleep

print('''
▀████    ▐████▀  ▄█   ▄█        ▄█          ▄████████ ███▄▄▄▄   
  ███▌   ████▀  ███  ███       ███         ███    ███ ███▀▀▀██▄ 
   ███  ▐███    ███▌ ███       ███         ███    █▀  ███   ███ 
   ▀███▄███▀    ███▌ ███       ███        ▄███▄▄▄     ███   ███ 
   ████▀██▄     ███▌ ███       ███       ▀▀███▀▀▀     ███   ███ 
  ▐███  ▀███    ███  ███       ███         ███    █▄  ███   ███ 
 ▄███     ███▄  ███  ███▌    ▄ ███▌    ▄   ███    ███ ███   ███ 
████       ███▄ █▀   █████▄▄██ █████▄▄██   ██████████  ▀█   █▀  
       By @TheDarkW3b              ▀         ▀                                
''')
print("\nMust Read README.txt Before Using....\n")

print("Invite Link Example : https://t.me/joinchat/AAAAAFFszQPyPEZ7wgxLte\n")
channel = input("Enter Channel Invite Link :- ")
new_link = channel.split("/")
try:
    os.chdir("sessions")
except:
    print("\nFolder Named 'sessions' Not Found.... Exiting ...")
    sleep(3)
    exit()

sfiles = []
for files in glob.glob("*.session"):
    sfiles.append(files)

total_len = len(sfiles)
if total_len == int(0):
    print("\nNo Sessions In 'sessions' Folder.. First Run Sessions Creator.exe and Create sessions")
    sleep(3)
    exit()

print(f"\nTotal {total_len} Session Files Found\n")
indexx = 0
while indexx < total_len:
    document_name = sfiles[indexx]
    indexing = document_name.split(".")
    session_name = indexing[0]
    client = TelegramClient(session_name, api_id=1170033,
                            api_hash="5b2875309174291a0d6e03802e6c58c2").start()
    try:
        client(ImportChatInviteRequest(new_link[4]))
        print(f"Joined With {session_name}")
    except Exception as e:
        print(e)
        print("Invite Link Is Revoked... or Fix Session Later by Creating A new one")
        print(f"Skipping {session_name} ...\n")
        continue
    indexx += 1

input("Press Enter To Exit :-) ")