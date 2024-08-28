#URLLIB LIB
from urllib import request, parse

#HEADER
header_request = {"User-Agent": "paste_web_browser",
                "Cookie": "paste_cookie"}

#DATA
data_request = {"user": "paste_user", "password": "paste_pass"}
data_request = parse.urlencode(data_request).encode()

#REQUEST
req = request.Request("http://www.bancocn.com/admin/index.php", headers=header_request, data=data_request)
resp = request.urlopen(req)
html = resp.read()
print(html)
