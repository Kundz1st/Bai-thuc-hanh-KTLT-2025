print("Sinh viên: Lang Văn Doan")
print(" MSSV: 235752020710023")
ds = input('Nhap chuoi:').split()
#Yêu cầu người dùng nhập một chuỗi
#.split() tách chuỗi thành danh sách các phần, mặc định tách theo khoảng trắng
ds.append('abc')
#.append() để thêm phần tử 'abc' vào cuối danh sách
for ch in ds:
#Duyệt qua từng phần tử trong danh sách ds
    print(ch)
    #In từng phần tử ra mỗi dòng một từ.
print("sinh vien: Lang Van Doan")
print("Mssv: 235752020710023")