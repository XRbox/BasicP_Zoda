# def grade(score):
#     if score > 79:
#         print("A")
#     elif score > 69:
#         print("B")
#     elif score > 59:
#         print("C")
#     elif score > 49:
#         print("D")
#     else:
#         print("F")

# x = "สวัสดี"

# score1 = int(input("ใส่คะแนนของคุณซะ : "))
# grade(score1)
# print(x)

# def my_sum(a):
#     return a + 20

# result = my_sum(int(input("ใส่ข้อมูลตัวเลข : ")))
# print(result)

# def cal_price(a ,b): # Business Logic
#     first_cal = a*b
#     result = first_cal * 0.07
#     result += first_cal
#     return result    
# def choose_menu(): #UI , User Interface
#     while True:
#         choose = int(input("เลือก 1 ไม่ก็ 2 : "))
#         if choose == 1:
#             how_some = int(input("กี่อัน : "))
#             how_price = int(input("ราคาเท่าไร : "))
#             x = (cal_price(how_some, how_price))
#             print("x is : ",x)

#         elif choose == 2:
#             print("Bye")
#             break

# choose_menu()

# x = ["1", 2, "3.14"]
# print(x[0])
# x[0] = 3
# print(x[0])


# x = [1 ,2 ,3 ,4]
# for i in x:
#     print(i)

# my_dict = {
#     "name" : "zoda" ,
#     "age" : 18 ,
#     "hobby" : "play_game"
# }

# my_dict["Study]"] = "KMUTT"
# my_dict["age"] = 13
# print(my_dict["age"])
# print(type(my_dict["age"]))

students = [
    {"name" : "zoda" , "age" : 18 , "IT" : 31},
    {"name" : "net" , "age" : 18 , "IT" : 31},
    {"name" : "gap" , "age" : 20 , "IT" : 29}
]
for student in students:
    if (student["age"] >= 19):
        student["age"] = "old"
    else:
        student["age"] = "young"
    print(student)
