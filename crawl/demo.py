import requests

url = 'http://example.com/userinfo.php'
values = {'email': 'admin',
          'password': '123456aA'}

r = requests.post('http://45.79.43.178/source_carts/wordpress/wp-admin/', data=values)
print(r.status_code)
print(r.cookies.get_dict())