# 1.login vào site http://45.79.43.178/source_carts/wordpress/wp-admin bằng code python. Sau khi login thành công thì lấy ra name của user vừa login
# email': 'admin', 'password': 123456aA
# làm theo 2 cách:
# 	- dùng requests. (Gợi ý: chú ý cookie trong request header)
# 	- dùng selenium

import requests

url = 'http://example.com/userinfo.php'
values = {'email': 'admin',
          'password': '123456aA'}

r = requests.post('http://45.79.43.178/source_carts/wordpress/wp-admin/', data=values)
print(r.status_code)
print(r.cookies.get_dict())