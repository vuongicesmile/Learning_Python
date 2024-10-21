# khong the thay doi phan tu trong tuples

day_so = (1,2,3,4,5,6)
# thay doi dau [] thay dau ()
# khi muon thao tac voi danh sach ma ko muon thay doi danh sach do

#ky thuat unpacking
day_so_test = (1,2,3)
tich = day_so_test[0] * day_so_test[1] * day_so_test[0]

# => ky thuat unpacking

x,y,z = day_so_test
tich1 = x * y * z
print(tich1)



