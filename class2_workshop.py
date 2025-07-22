#สงครามรันด่วน
Distance = int(input("ระยะทางของคุณเท่าไร : "))

if Distance < 0: 
    print("ส่งย้อนกลับหรอไอขี้หมา")
elif Distance <= 50 and Distance > 4:
    print("10 บาท")
elif Distance <= 100 and Distance > 50:
    print("15 บาท")
elif Distance <= 300 and Distance > 100:
    print("25 บาท")
elif Distance <= 500 and Distance > 300:
    print("35 บาท")
elif Distance > 500 :
    print("45 บาท")
else:
    print("ไม่ส่งให้พวกขี้หมา")
