print("Sinh viên: Lang Văn Doan")
print(" MSSV: 235752020710023")
ds = input('Nhap chuoi:').split()
#input(...): yêu cầu người dùng nhập một dòng văn bản.
#.split(): tách chuỗi đó thành các phần tử (tách theo khoảng trắng).
ds.remove('123')
#Dòng này tìm và xóa phần tử '123' đầu tiên xuất hiện trong danh sách, nếu không có sẽ báo lỗi
for ch in ds:
#Duyệt từng phần tử trong danh sách ds
    print(ch)
print("sinh vien: Lang Van Doan")
print("Mssv: 235752020710023")