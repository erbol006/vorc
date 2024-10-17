class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль невозможно.")
        return self.value / other.value

# Пример использования
if __name__ == "__main__":
    calc1 = Calculator(10)
    calc2 = Calculator(5)

    print(f"Сложение: {calc1 + calc2}")
    print(f"Вычитание: {calc1 - calc2}")
    print(f"Умножение: {calc1 * calc2}")
    print(f"Деление: {calc1 / calc2}")
