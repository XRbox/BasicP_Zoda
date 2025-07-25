def loop(num):
    menu_list = [
        {'name' : 'น้ำปั่นรองเท้าแตะ','price' : 10},
        {'name' : 'น้ำแมลงปอปั่น' , 'price' : 15},
        {'name' : 'น้ำพี่gapพูดไรwa' , 'price' : 20},
        {'name' : 'น้ำปั่นรวมมิตรเอเลี่ยนจากมิติ nown' , 'price' : 10000},
        {'name' : 'น้ำระดมพล' , 'price' : 20},
        {'name' : 'น้ำ compro ยำ IT fun โรยด้วย devtool', 'price' : 30}]
    
    topping = [
        {'name' : 'ถั่วอาบรังสี','price' : 5},
        {'name' : 'เฉาก๊วยชากังราว' , 'price' : 10},
        {'name' : 'ขี้ไคลพระบิดา' , 'price' : 'FREE'}]
    
    sweet = [
        {'name' : '150%','price' : 10},
        {'name' : '100%' , 'price' : 'FREE'},
        {'name' : '50%' , 'price' : -5}]
    
    size = [
        {'name' : 'S','price' : 40},
        {'name' : 'M' , 'price' : 60},
        {'name' : 'L' , 'price' : 85}]

    results = 0
    for i in range(num):
        show_list(menu_list)
        choice = int(input("เลือกเมนูที่ต้องการ : ")) - 1
        checkInList(choice , menu_list)
        show_list(sweet)
        choice_sweet = int(input("เลือกความหวานตัดขาของคุณเลย : ")) - 1
        checkInList(choice_sweet , sweet)
        show_list(topping)
        choice_topping = int(input("เลือกท็อปปิ้งที่คุณต้องการ : ")) - 1
        checkInList(choice_topping , topping)
        show_list(size)
        choice_size = int(input("เลือกขนาดที่คุณต้องการ : ")) - 1
        checkInList(choice_size , size)
        results += calculator(menu_list[choice]['price'] , sweet[choice_sweet]['price'] , topping[choice_topping]['price'] , size[choice_size]['price'])
        print(f"รายการที่ต้องชำระคือ : {menu_list[choice]['name']}\n เพิ่ม : {topping[choice_topping]['name']}\n หวาน : {sweet[choice_sweet]['name']}\n ขนาด : {size[choice_size]['name']}")
        dot_line()
    return results
def main():
    quan = int(input("สั่งกี่แก้ว : "))
    result = loop(quan)
    dot_line()
    print("ราคารวมคือ" , result)

def show_list(lists):
    for i ,list in enumerate(lists):
        print(f"{i +  1}" , list['name'] , list['price'])
    dot_line()


def calculator(price_menu , price_sweet , price_topping , price_size):
    if price_sweet == 'FREE':
        price_sweet = 0
    if price_topping == 'FREE':
        price_topping = 0
    result = (price_menu + price_sweet + price_topping + price_size)
    return result

def dot_line():
    print("-------------------------------")

def checkInList(input , listIndex):
    if  0 <= input  < len(listIndex):
        pass
    else:
        print("ขออภัยไม่ได้อยู่ในตัวเลือก โปรดกลับไปหน้าแรก")
        dot_line()
        main()
        



main()