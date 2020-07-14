from telethon.sync import TelegramClient
import os

print('''
▀████    ▐████▀  ▄█   ▄█        ▄█          ▄████████ ███▄▄▄▄   
  ███▌   ████▀  ███  ███       ███         ███    ███ ███▀▀▀██▄ 
   ███  ▐███    ███▌ ███       ███         ███    █▀  ███   ███ 
   ▀███▄███▀    ███▌ ███       ███        ▄███▄▄▄     ███   ███ 
   ████▀██▄     ███▌ ███       ███       ▀▀███▀▀▀     ███   ███ 
  ▐███  ▀███    ███  ███       ███         ███    █▄  ███   ███ 
 ▄███     ███▄  ███  ███▌    ▄ ███▌    ▄   ███    ███ ███   ███ 
████       ███▄ █▀   █████▄▄██ █████▄▄██   ██████████  ▀█   █▀  
            By @TheDarkW3b         ▀         ▀                                
''')
print("\nMust Read README.txt Before Using....\n")

try:
    os.mkdir("sessions")
except:
    pass

repeat = 1

while (repeat == int(1)):
    try:
        change_dir = os.chdir("sessions")
    except:
        pass
    phone = input("Enter Phone Number with Country Code :- ")
    api_id = int(input("Enter API_ID :- "))
    api_hash = input("Enter API_HASH :- ")

    client = TelegramClient(phone, api_id=api_id, api_hash=api_hash)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter The Code Sent To Your Telegram Login :- '))

    me = client.get_me()

    print(f"\nSuccesfully Created Session :- {me.phone}\n")

    repeat = int(input("Enter 1 To Create More Sessions and 0 to exit :- "))

