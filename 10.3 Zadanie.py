
from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            cash = randint(50, 500)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += cash
            print(f'Пополнение: {cash}. Баланс: {self.balance}')
        

    def take(self):
        for i in range(100):
            cash = randint(50, 500)
            print(f"Запрос на {cash}")
            if cash <= self.balance:
                self.balance -= cash
                print(f"Снятие: {cash}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
        sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

