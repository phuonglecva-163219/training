# 2. Đọc file customer.csv sau đó lưu hết vào database. Yêu cầu:
# 	- Database dùng mysql
# 	- Database được tạo trước
# 	- Table sẽ được tự động tạo khi chạy
import datetime
import csv 
import mysql.connector

user = "phuonglc"
password = "1111"
dbName = 'my_database'
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user=user,
    password=password,
    database=dbName
)

myCursor = mydb.cursor()
myCursor.execute("drop table if exists customer")
myCursor.execute("create table customer (customerid int primary key,firstname varchar(255),lastname varchar(255),companyname varchar(255),billingaddress1 varchar(255),billingaddress2 varchar(255),city varchar(255),state varchar(10),postalcode varchar(50),country varchar(25),phonenumber varchar(15),emailaddress varchar(200),createddate datetime)")
# print(myCursor)
# csv file name 
filename = "customer.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
    
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 

sql = "insert into customer values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
for row in rows:
    row[-1] = datetime.datetime.strptime(row[-1], '%d/%m/%Y %H:%M')

myCursor.executemany(sql, rows)
mydb.commit()
print(myCursor.rowcount, "was inserted.")
