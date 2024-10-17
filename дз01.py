class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount
        print(f"Ваш новый баланс: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Ваш баланс обнулен.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Ваш новый баланс после джекпота: {self._balance}")

    def _combine_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            other._balance = 0
            print(f"Баланс объединен. Ваш новый баланс: {self._balance}")

# Пример использования
if __name__ == "__main__":
    client1 = Bank("Клиент 1", 100)
    client2 = Bank("Клиент 2", 200)

    client1.moneyX()
    client1._combine_balance(client2)
    client1._kill()
