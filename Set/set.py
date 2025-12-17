# Tạo set

my_set = {'a', 'b', 'c', 'd'}  # Khi in ra các element sẽ không theo thứ tự
# my_set = set() ==> Tập rỗng
# Thêm phần tử
my_set.add('e') # ==> 'e' random trong tập set

# Xóa phần tử
my_set.discard('a')  # ==> 'a' mất trong set

# Biểu đồ venn
my_set_1 = {'a', 'b', 'c', 'd'}
my_set_2 = {'c', 'd', 'e', 'f'}

# new_set = my_set_1.intersection(my_set_2)  # ==> {'c','d'}
# Others way
# new_set = my_set_1 | my_set_2   ==> Intersection = |

# new_set = my_set_1.union(my_set_2)  # ==> {'a', 'b', 'c', 'd', 'e', 'f'}
# new_set = my_set_1 & my_set_2   ==> Union = &

# new_set = my_set_1.symmetric_difference(my_set_2)  # ==> {'a', 'b', 'e', 'f'}
# new_set = my_set_1 ^ my_set_2   ==> Symmetric difference = ^

# new_set = my_set_1.difference(my_set_2)  # ==> {'a', 'b'}
# new_set = my_set_2.difference(my_set_1)  # ==> {'e', 'f'} Ai đứng trước lấy trước
# new_set = my_set_2 - my_set_1   ==> difference = -