while True:
    monster = 0 
    kiritu_shadow = 40 #พี่ไอซ์บอกท้าทายตัเองให้ทำมา 3 ตัว
    goblin = 20
    slime = 5
    sword = 5
    pike = 3
    bow = 2
    menu = int(input("1 for fight , 2 for out : ")) #เลือกว่าจะสู้หรือจะหนี
    if menu == 1:
        print("เลือก 1 เพื่อสู้กับ kiritu_shadow เลือด(40)")
        print("เลือก 2 เพื่อสู้กับ goblin เลือด(20)")
        print("เลือก 3 เพื่อสู้กับ Slime เลือด(5)")
        choose_monster = int(input("เลือก 1-3 : "))#เลือกว่าจะสู้ตัวไหนดี
        if choose_monster == 1:
            print("คุณเลือกตีเงาคิริตู่")
            atk_round = int(input("กรอกจำนวนรอบ : ")) #จำนวนรอบที่ตี
            sum_atk = 0

            for i in range(atk_round):
                print("-----รอบที่ ", i + 1 ,"-----")
                choose_weapon = int(input("1. ดาบ(5) 2. หอก(3) 3. ธนู(2) : "))
                if choose_weapon == 1:
                    kiritu_shadow = kiritu_shadow - sword
                    sum_atk += sword
                    print("โจมตีรวม :" , sum_atk)
                    if kiritu_shadow < 0:
                        kiritu_shadow = 20
                    print("เลือดเหลือ : " , kiritu_shadow)
                    monster = kiritu_shadow
                elif choose_weapon  == 2:
                    kiritu_shadow = kiritu_shadow - pike
                    sum_atk += pike
                    print("โจมตีรวม :" , sum_atk)
                    if kiritu_shadow < 0:
                        kiritu_shadow = 20
                    print("เลือดเหลือ : " , kiritu_shadow)
                    monster = kiritu_shadow
                elif choose_weapon == 3:
                    kiritu_shadow = kiritu_shadow - bow
                    sum_atk += bow
                    print("โจมตีรวม :" , sum_atk)
                    if kiritu_shadow < 0:
                        kiritu_shadow = 20
                    print("เลือดเหลือ : " , kiritu_shadow)
                    monster = kiritu_shadow

        if choose_monster == 2:
            print("คุณเลือกตีก็อปลิน")
            atk_round = int(input("กรอกจำนวนรอบ : "))
            sum_atk = 0

            for i in range(atk_round):
                print("-----รอบที่ ", i + 1 ,"-----")
                choose_weapon = int(input("1. ดาบ(5) 2. หอก(3) 3. ธนู(2) : "))
                if choose_weapon == 1:
                    goblin = goblin - sword
                    sum_atk += sword
                    print("โจมตีรวม :" , sum_atk)
                    if goblin < 0:
                        goblin = 20
                    print("เลือดเหลือ : " , goblin)
                    monster = goblin
                elif choose_weapon  == 2:
                    goblin = goblin - pike
                    sum_atk += pike
                    print("โจมตีรวม :" , sum_atk)
                    if goblin < 0:
                        goblin = 20
                    print("เลือดเหลือ : " , goblin)
                    monster = goblin
                elif choose_weapon == 3:
                    goblin = goblin - bow
                    sum_atk += bow
                    print("โจมตีรวม :" , sum_atk)
                    if goblin < 0:
                        goblin = 20
                    print("เลือดเหลือ : " , goblin)
                    monster = goblin
        if choose_monster == 3:
            print("คุณเลือกตีสไลม์กากๆ")
            atk_round = int(input("กรอกจำนวนรอบ : "))
            sum_atk = 0

            for i in range(atk_round):
                print("-----รอบที่ ", i + 1 ,"-----")
                choose_weapon = int(input("1. ดาบ(5) 2. หอก(3) 3. ธนู(2) : "))
                if choose_weapon == 1:
                    slime = slime - sword
                    sum_atk += sword
                    print("โจมตีรวม :" , sum_atk)
                    if slime < 0:
                        slime = 20
                    print("เลือดเหลือ : " , slime)
                    monster = slime
                elif choose_weapon  == 2:
                    slime = slime - pike
                    sum_atk += pike
                    print("โจมตีรวม :" , sum_atk)
                    if slime < 0:
                        slime = 20
                    print("เลือดเหลือ : " , slime)
                    monster = slime
                elif choose_weapon == 3:
                    slime = slime - bow
                    sum_atk += bow
                    print("โจมตีรวม :" , sum_atk)
                    if slime < 0:
                        slime = 20
                    print("เลือดเหลือ : " , slime)
                    monster = slime

        if monster == 0: #ตายพอดี
            print("ชนะ เก่งมาก")
        elif monster < 0: #ติดลบเฉย
            print("แพ้ มอนเลือดรีกลับมา 20")
        elif monster > 0: #ไม่ตาย
            print("ตีไม่ตาย ตายเอง haha")

    elif menu == 2: #หนี ออกเกม
        print("ลาก่อน")
        break

