print("Sinh viên: Lang Văn Doan")
print(" MSSV: 235752020710023")
ds = input('Nhap chuoi:').split()
#Yêu cầu người dùng nhập một chuỗi
#.split() tách chuỗi thành danh sách các phần, mặc định tách theo khoảng trắng
x = ds[1:-1]
#ds[1:-1] là cắt danh sách từ phần tử thứ 2 đến trước phần tử cuối cùng (cắt đầu và cuối)
for c in x:
    #Duyệt qua từng phần tử trong danh sách x
    print(c)
    #In ra từng từ trên một dòng
print("sinh vien: Lang Van Doan")
print("Mssv: 235752020710023")