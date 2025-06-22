import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # Геттер для названия товаров    
    @property
    def name_items(self):
        return self.__name_items

    # Геттер для количества товаров    
    @property
    def number_items(self):
        return self.__number_items

    #Метод добавления товаров в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    # Метод удаления товаров из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # Метод для подсчёта общей суммы покупок
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        amount = sum(total)
        if len(self.__name_items) > 10:
            amount *= 0.9     
        return amount

    # Метод для расчёта НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        
        total_twenty_percent_tax = sum(total) * 0.2
        if len(self.__name_items) > 10:
            total_twenty_percent_tax *= 0.9
                
        return total_twenty_percent_tax

    # Метод для расчёта НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        
        total_ten_percent_tax = sum(total) * 0.1
        if len(self.__name_items) > 10:
            total_ten_percent_tax *= 0.9
                
        return total_ten_percent_tax

    # Метод для расчёта общей суммы НДС
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    # Статический метод возврата номера телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if len(telephone_number) < 10:
            raise ValueError('Необходимо ввести цифры') 
        if len(telephone_number) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'

    # Статический метод возврата даты и времени покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['секунды', lambda x: x.second],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        
        for unit_of_time, time in date:
            date_and_time.append(f"{unit_of_time}: {time(now)}")
        
        return date_and_time











