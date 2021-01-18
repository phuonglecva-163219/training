print("Hay nhap  gia tri x < y va x > 0")
while True:    
    x = int(input("Nhap vao gia tri x: "))
    y = int(input("Nhap vao gia tri y: "))
    if x < y and x > 0:
        break
    else:
        print("Hay nhap  gia tri x < y va x > 0")

if x > 0 and y < 0:
    print("So buoc la: {}".format(x - y))
elif y / x >= 2:
    print("So buoc la: {}".format(y - x * 2 + 1))
else:
    print("So buoc la: {}".format(x - y))