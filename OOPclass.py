class information : 
    def __init__(self , name , age , debt , number , status):
        self.name = name
        self.__age = age
        self.__debt = debt
        self.number = number
        self.status = status

    def show_data(self): #เรียกข้อมูลผู้เล่น
        print(f"ชื่อผู้เล่น : {self.name}")
        print(f"เลขผู้เล่น : {self.number}")
        print(f"สถานะผู้เล่น : {self.status}")
        print("--- --- ---")

    def show_hide_data(self): #ค่อยทำ ขก.
        pass

players = [] #เก็บข้อมูลผู้เล่นใน list

def add_player(): #Func เพิ่ม player
    num_player = int(input("กรอกจำนวนผู้เล่นที่จะเพิ่มเข้าไปในเกมนี้ : "))
    for i in range(num_player): #เอา num_player ไปเป็นขอบเขตใน loop
        print("---รายชื่อคนที่" , i + 1 , "---")
        name = input("ป้อนชื่อผู้เล่น : ")
        age = int(input("ใส่อายุของผู้เล่นคนนี้ : "))
        debt = int(input("ใส่หนี้ของผู้เล่นคนนี้ : "))
        number = int(input("ใส่หมายเลขของผู้เล่นคนนี้ : "))
        status = int(input("ใส่ 1 ถ้าผู้เล่นยังไม่เสียชีวิต ใส่ 2 หากผู้เล่นเสียชีวิตแล้ว : "))
        if status == 1:
            status = "alive"
        elif status == 2:
            status = "not alive"
        else:
            status = "ERROR"
        player = information(name , age , debt , number , status) #เก็บเข้า class
        players.append(player) #เก็บเข้า list
    print("ต้องการเพิ่มผู้เล่นอีกหรือไม่ 1.ใช่ 2.ไม่") #เช็คว่าจะเพิ่มผู้เล่นต่อไหม
    choice = int(input("1 or 2 : "))
    if choice == 1:
        add_player()
    else:
        main() #กลับ main

def main(): #Func หลัก
    print(f"เลือกว่า MR.FRONT MAN จะทำอะไร \n 1.เพิ่มผู้เล่น \n 2.จัดการสถานะผู้เล่น \n 3.โชว์ข้อมูลผู้เล่นทั้งหมด \n 4.ออกจากโปรแกรม")
    choice = int(input("1 2 3 or 4 : "))
    if choice == 1: #เพิ่มผู้เล่น
        add_player()
    elif choice == 2: #แก้ข้อมูลผุู้เล่น
        fix_data()
    elif choice == 3: #โชว์ผู้เล่นทั้งหมดและข้อมูล
        show_all_player()
    elif choice == 4: #ออกโปรแกรม
        pass
    print("--BYE--BYE--")

def fix_data(): #Func แก้สถานะ
    for i, s in enumerate(players, start=1):
        print(f"คนที่ {i}")
        s.show_data() #show ข้อมูลของแต่ละคนก่อน
    
    index = int(input("ต้องการแก้สถานะของใคร : ")) #เลือกว่าแก้ของใคร
    new_status = int(input("ใส่ 1 ถ้าผู้เล่นยังไม่เสียชีวิต ใส่ 2 หากผู้เล่นเสียชีวิตแล้ว : ")) #แก้เป็นอะไร
    if new_status == 1:
        new_status = "alive"
    elif new_status == 2:
        new_status = "not alive"
    else:
        new_status = "ERROR"
    players[index - 1].status = new_status
    print("ต้องการแก้ผู้เล่นอีกหรือไม่ 1.ใช่ 2.ไม่") #จะแก้คนอื่นอีกไหม
    choice = int(input("1 or 2 : "))
    if choice == 1:
        fix_data() #ถ้าแก้ก็กลับ Func fix_data
    else:
        main() #ไม่ก็กลับ main
        

def show_all_player(): #func เรียกข้อมูลผู้เล่น
    print("--- ผู้เล่นทั้งหมด ---")
    for p in players:
        p.show_data()
    main() #โชว์เสร็จกลับ main


print("ยินดีต้อนรับคุณ FRONT MAN เข้าสู่ระบบควบคุม")
main()