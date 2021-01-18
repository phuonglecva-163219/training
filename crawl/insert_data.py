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
myCursor.execute("create table customer (customerid int primary key,firstname varchar(255),lastname varchar(255),companyname varchar(255),billingaddress1 varchar(255),billingaddress2 varchar(255),city varchar(255),state,postalcode,country,phonenumber ,emailaddress,createddate)")

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

for row in rows:
    print(row)