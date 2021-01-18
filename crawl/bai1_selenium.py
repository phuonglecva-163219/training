from selenium import webdriver

DRIVER_PATH = '/home/phuonglc/Downloads/setup/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
login_data = {
    'log': 'admin',
    'pwd': '123456aA',
}
# driver.request('POST', 'http://45.79.43.178/source_carts/wordpress/wp-login.php', data=login_data)
# print(driver)
driver.get("http://45.79.43.178/source_carts/wordpress/wp-login.php")
# print(driver.page_source)

username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("user_pass")

username.send_keys("admin")
password.send_keys("123456aA")

form = driver.find_element_by_id('loginform')
form.submit()

divs = driver.find_element_by_class_name('quicklinks')

name = driver.find_element_by_xpath("//div[@class='quicklinks']//li[@id='wp-admin-bar-my-account']//a")
print("Username : {}".format(name.text))