# 3. Truy cập theo địa chỉ https://www.shopify.com tạo 1 site test (click start free trial)
# Login vào site test vừa tạo, lấy info APi theo hướng dẫn: https://litextension.com/migration-guides/how-to-get-api/get-api-from-shopify
# vào tab customer tạo thử 1 vài customer 
# Lấy customer từ site vừa tạo sử dụng api, lưu ra file
# 	- lấy hết customer về, lưu vào 1 file csv, bỏ qua k cần lưu addresss
# 	- docs: 
# https://shopify.dev/tutorials/authenticate-a-private-app-with-shopify-admin#make-authenticated-requests
# https://shopify.dev/docs/admin-api/rest/reference/customers/customer#index-2020-04
# import shopify
# shop_url = "https://phuonglc-store.myshopify.com/admin" % ()
# site = shopify.ShopifyResource.set_site(shop_url)
# print(site)
import shopify
shopify.ShopifyResource.set_site("https://phuonglc-store.myshopify.com/admin/api/2021-01")
shopify.ShopifyResource.set_user('2318600785f6cd5c0d5aae2db652f4bd')
shopify.ShopifyResource.set_password('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')

customers = shopify.Customer.find()
list_attribute = []
data = []
customers_datas = []
for attr in customers[0].attributes:
    list_attribute.append(attr)
for customer in customers:
    # print(customer.attributes)
    data.append(customer.attributes)
    customers_datas.append([customer.attributes[att] for att in customer.attributes])

import csv
fields = list_attribute
    
# data rows of csv file  
rows = customers_datas
    
# name of csv file  
filename = "customers_shopifies.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 