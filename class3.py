# have_rice = False
# have_spoon = False

# if have_rice:
#     print("มีข้าว")
#     if have_spoon:
#         print("กินข้าว")
#     else:
#         print("กินไม่ได้")
# else:
#     print("กินอะไรไม่มีข้าว")

# score = int(input("ใส่คะแนนของคุณ : "))

#ก็อปพี่ gap
# if score >= 0:
#     if score <= 100:
#         if score >= 80:
#             print("A")
#         if score >= 70:
#             if score < 80:
#                 print("B")
#         if score >= 60:
#             if score < 70:
#                 print("C")
#         if score >= 50:
#             if score < 60:
#                 print("D")
#         if score < 50:
#             print("F")


#กลั้นกรอง
# if score <= 100:
#     if score >= 0:
#         if score < 50:
#             print("F")
#         if score >= 50:
#             if score < 60:
#                 print("D")
#         if score >= 60:
#             if score < 70:
#                 print("C")
#         if score >= 70:
#             if score < 80:
#                 print("B")
#         if score >= 80:
#             print("A")

#ลองใช้ Loop GPT_gen
# grades = ["F", "D", "C", "B", "A"]
# limits = [0, 50, 60, 70, 80]

# score = int(input())
# if score >= 0:
#     if score <= 100:
#         i = 0
#         for limit in limits:
#             if score >= limit:
#                 i = i + 1
#         print(grades[i - 1])


# Try pyramid , LOOP
# num = int(input())
# for i in range(num):
#     space = ' ' * (num - i - 1)
#     stars = '* ' * (i + 1)
#     print(space + stars)

# num = int(input())
# for i in range(num):
#     space = ' ' * (num - i - 1)
#     star = '*' * (2 * i +1)
#     print(space + star)

while True:
    choice = int(input("กรอก 1 เพื่อบวกเลข , กรอก 2 เพื่อออก "))
    if choice == 1:
        num = int(input("จำนวนเลขที่ต้องการจะบวก : "))
        sumation = 0

        for i in range(num):
            nam1 = int(input("กรอกเลข : "))
            sumation = sumation + nam1
        
        print("ผลลัพธ์ ", sumation)

    elif choice == 
        print("ลาก่อน")
        break
