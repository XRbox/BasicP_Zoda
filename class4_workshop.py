# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    for movie in movie_list:
        print(movie['movie_name'], movie['ticket_price'])
    return
        
# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    if age_restriction == 'G':
        return
    else:
        if user_age >= int(age_restriction):
            return
        else:
            print("-----------------------")
            print("อายุไม่ถึงให้เลือกดหนังเรื่องอื่น")
            print("-----------------------")
            main()
            


# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if genre == 'Sci-Fi':
        base_price += 50
        return base_price
    else:
        return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    show_movies(movie_list)
    print("-----------------------")
    choice = int(input("เลือก 1-5 เรื่องนี้ : "))
    choice -= 1
    print("-----------------------")
    age = int(input("โปรดใส่อายุของคุณ : "))
    check_age(age , movie_list[choice]['age_restriction'])
    print("-----------------------")
    soundtrack = input("จะดูsoundtrackหรือพากย์ไทย : ")
    price = (calculate_price(movie_list[choice]['ticket_price'] ,movie_list[choice]['genre']))
    print("-----------------------")
    print(movie_list[choice]['movie_name'] , soundtrack , price)

def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    menu = int(input("เลือก 1 เพื่อดูรายการหนัง 2 เพื่อเลือกซื้อตั๋วหนัง: "))
    if menu == 1:
        show_movies(movies)
    elif menu == 2:
        buy_ticket(movies)

# เรียก main เพื่อเริ่มโปรแกรม
main()