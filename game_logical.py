import random

class ГенераторЧисел:
    @staticmethod
    def отримати_випадкове_число():
        return random.randint(1, 100)

class ПеревіркаЧисла:
    @staticmethod
    def перевірити(введене_число, загадане_число):
        if введене_число < загадане_число:
            return "Загадане число більше."
        elif введене_число > загадане_число:
            return "Загадане число менше."
        else:
            return f"Вітаємо! Ви вгадали число {загадане_число}."

class ВведенняГравця:
    @staticmethod
    def отримати_введене_число():
        while True:
            введене_число = input("Спробуйте вгадати число від 1 до 100: ")

            try:
                введене_число = int(введене_число)
                return введене_число
            except ValueError:
                print("Введіть дійсне число!")

class Гра:
    def __init__(self):
        self.генератор_чисел = ГенераторЧисел()
        self.перевірка_числа = ПеревіркаЧисла()
        self.введення_гравця = ВведенняГравця()

    def почати(self):
        загадане_число = self.генератор_чисел.отримати_випадкове_число()
        спроби = 0

        while True:
            спроби += 1
            введене_число = self.введення_гравця.отримати_введене_число()

            результат = self.перевірка_числа.перевірити(введене_число, загадане_число)
            self.вивести_результат(результат)

            if результат.startswith("Вітаємо!"):
                self.вивести_кількість_спроб(спроби)
                self.перезапустити_гру()

    @staticmethod
    def вивести_результат(результат):
        print(результат)

    @staticmethod
    def вивести_кількість_спроб(спроби):
        print(f"Ви вгадали число за {спроби} спроб.")

    def перезапустити_гру(self):
        відповідь = input("Чи бажаєте ви перезапустити гру? (так/ні): ")

        if відповідь.lower() == "так":
            self.почати()
        else:
            print("Дякуємо за гру! До побачення.")

# Запуск гри
гра = Гра()
гра.почати()
