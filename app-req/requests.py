#REQUEST LIB
import requests

#HEADER
header_request = {"User-Agent": "paste_web_browser",
             "Cookie": "paste_cookie"}

#DATA
data_request = {"user": "paste_user", "password": "paste_pass"}

#RESPONSE
resp = requests.post("paste_link", headers=header_request, data=data_request)
html = resp.text
print(html)
