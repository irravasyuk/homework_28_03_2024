# Завдання 1
# class Device:
#     def __init__(self, brand, year, model):
#         self._brand = brand
#         self._year = year
#         self._model = model
#
#     def information(self):
#         return f"\nInformation:\nBrand: {self._brand}\nYear: {self._year}\nModel: {self._model}"
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, year, model, coffe):
#         super().__init__(brand, year, model)
#         self._coffe = coffe
#
#     def make_coffe(self):
#         print(f"{self._brand} {self._model} is making {self._coffe}")
#
# class Blender(Device):
#     def __init__(self, brand, year, model, type_of_blender):
#         super().__init__(brand, year, model)
#         self._type_of_blender = type_of_blender
#
#     def info(self):
#         print(f"{self._brand} {self._model} is {self._type_of_blender} blender type")
#
# class MeatGrinder(Device):
#     def __init__(self, brand, year, model, power):
#         super().__init__(brand, year, model)
#         self._power = power
#
#     def power_of_the_meatgrinder(self):
#         print(f"{self._brand} {self._model} has a power of {self._power}")
#
# coffemachine = CoffeeMachine("Suzhou Dr. Coffee System Technology Co", 2023, "Dr. Coffee F22", "all drinks with and without milk")
# print(coffemachine.information())
# coffemachine.make_coffe()
#
# blender = Blender("Philips", 2022, "Series 5000 HR2228/90", "stationary")
# print(blender.information())
# blender.info()
#
# meatgrinder = MeatGrinder("Esperanza", 2023, "EKM012E", "1200W")
# print(meatgrinder.information())
# meatgrinder.power_of_the_meatgrinder()

# Завдання 3
# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число. Для кожного з класів реалізуйте необхідні методи та поля.
class Money:
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents

    def display(self):
        return f"{self._dollars}.{self._cents:02} $"

    def set_amount(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents

class Product(Money):
    def __init__(self, dollars, cents, name):
        super().__init__(dollars, cents)
        self._name = name

    def reduce_price(self, dollars, cents):
        total_cents = self._dollars * 100 + self._cents
        discount = dollars * 100 + cents
        total_cents -= discount
        if total_cents < 0:
            print("Error: Price cannot be negative.")
        self._dollars = total_cents // 100
        self._cents = total_cents % 100

    def increase_price(self, dollars, cents):
        total_cents = self._dollars * 100 + self._cents
        increase = dollars * 100 + cents
        total_cents += increase
        if total_cents < 0:
            print("Error: Price cannot be negative.")
        self._dollars = total_cents // 100
        self._cents = total_cents % 100

    def __str__(self):
        return f"Product: {self._name}\nPrice: {self._dollars}.{self._cents} $"

product = Product(500, 50, "Phone")
print(product)
print("Price after discount:")
product.reduce_price(100, 40)
print(product)
print("Price after increase price:")
product.increase_price(200, 10)
print(product)







