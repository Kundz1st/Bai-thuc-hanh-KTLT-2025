def file_append_and_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("21thanhhung\n")
        myfile.write("18032005\n")
    with open(fname, "r") as txt:
        print(txt.read())
file_append_and_read('kunz.txt')
print("sinh vien: Lang Van Doan")
print("Mssv: 235752020710023")