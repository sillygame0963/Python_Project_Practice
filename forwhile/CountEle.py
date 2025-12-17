# Đếm kí tự trong chuỗi

my_str = "xin chao cac ban"
my_dict = {}

for char in my_str:
    if char == " ":
        continue
    else:
        if char not in my_dict.keys():
            my_dict[char] = 1
        else:
            my_dict[char] += 1

print(my_dict)