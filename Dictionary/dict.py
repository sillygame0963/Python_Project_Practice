# Định nghĩa
# Khởi tạo dictionary
# name_age = {"Son": 22, "Thu": 23}
# Tạo dictionary rỗng
# name_age = dict()
# name_age = {}

# # Truy cập
# print(name_age["Son"])  # ==> 22
#
# # Thêm vào dict, update giá trị
# name_age["Thu"] = 18  # ==> "Thu": 18 (update dictionary)
# name_age["Trung"] = 16 # ==> {"Son": 22, "Thu": 23, "Trung": 16} (add into dictionary)

# # Duyệt qua các phần tử
# name_age = {"Son": 22, "Thu": 23}
# # Duyệt keys
# # for k in name_age:
# # for k in name_age.keys():  # giống câu trên
# #     print(k)
#
# # Duyệt value
# # for k in name_age.values():
# #     print(k)
#
# # Duyệt cả 2
# for k, v in name_age.items():  # Dùng .items() để duyệt cả 2
#     print(k,v)




"""Tính điểm trung bình từng môn"""

students = [
    {"id": 1, "Name": "Nguyen Thai Son", "Score": {"math": 8, "chemistry": 10, "english": 10}},
    {"id": 2, "Name": "Nguyen Thanh An", "Score": {"math": 7, "chemistry": 9, "english": 5}}
]

total_math = 0
total_chemistry = 0
total_english = 0

for stu in students:
    total_math += stu["Score"]["math"]
    total_chemistry += stu["Score"]["chemistry"]
    total_english += stu["Score"]["english"]

num_stu = len(students)
print(num_stu)

avg_math = total_math / num_stu
avg_chemistry = total_chemistry / num_stu
avg_english = total_english / num_stu

print(f"Average score of math is: {avg_math}")
print(f"Average score of chemistry is: {avg_chemistry}")
print(f"Average score of english is: {avg_english}")