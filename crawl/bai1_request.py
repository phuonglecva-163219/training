# 1.login vào site http://45.79.43.178/source_carts/wordpress/wp-admin bằng code python. Sau khi login thành công thì lấy ra name của user vừa login
# email': 'admin', 'password': 123456aA
# làm theo 2 cách:
# 	- dùng requests. (Gợi ý: chú ý cookie trong request header)
# 	- dùng selenium

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
login_data = {
    'log': 'admin',
    'pwd': '123456aA',
}

with requests.Session() as s:
    url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
    site = s.post(url, headers=headers, data=login_data)
    soup = BeautifulSoup(site.content, "lxml")
    mydivs = soup.findAll("div", {"class": "quicklinks"})
    username = mydivs[0].findAll("li", {'class':'with-avatar'})[0].find("a").text
    print("Username: {}".format(username))