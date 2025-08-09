class Room:
    def __init__(self, number: int, price: int):
        self.number = number # номер номер
        self.price = price # цена за ночь
        self.is_booked = False # Занят ли номер

class Guest:
    def __init__(self, name: str):
        self.name = name # Имя пользователя

class Hotel:
    def __init__(self, name: str):
        self.name = name # Имя отеля
        self.rooms = [] # Номера
    def add_room(self, room: Room): # добавление номера из класса Room
        self.rooms.append(room) 
    def booking(self, guest: Guest, room_number: int, number_of_days: int): # Бронирование
        if number_of_days <= 0:
            print("Ошибка: количество дней должно быть положительным!")
        for room in self.rooms:
            if room.number == room_number:
                if room.is_booked:
                    print("Номер уже занят!")
                else:
                    room.is_booked = True
                    if number_of_days == 1 or number_of_days == 21: # Если 1 или 21 - день
                        print(f"{guest.name} забронировал номер {room.number} на {number_of_days} день, цена {room.price * number_of_days} руб.")
                    elif number_of_days > 1 and number_of_days < 5: # Если больше двух и меньше пяти - дня
                        print(f"{guest.name} забронировал номер {room.number} на {number_of_days} дня, цена {room.price * number_of_days} руб.")
                    elif number_of_days > 5 or number_of_days == 5: # Если больше или равно пяти - дней
                        print(f"{guest.name} забронировал номер {room.number} на {number_of_days} дней, цена {room.price * number_of_days} руб.")
                return
        print("Номер не найден!")
    def cancel_booking(self, room_number: int): # Отменяем бронь
        for room in self.rooms:
            if room.number == room_number:
                if room.is_booked:
                    room.is_booked = False
                    print(f"Бронь номера {room.number} отменена")
                else:
                    print(f"Номер {room.number} свободен")
                return
        print("Номер не найден!")

# Пример работы

hotel = Hotel("Grand")

hotel.add_room(Room(101, 5000))
hotel.add_room(Room(102, 12000))

guest1 = Guest("Иван")
guest2 = Guest("Мария")

hotel.booking(guest1, 101, 2)
hotel.booking(guest2, 102, 6)

hotel.cancel_booking(101)