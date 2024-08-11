from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self, lock=threading.Lock(), balance=randint(50, 500)):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            cash = randint(50, 500)
            self.balance += cash
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {cash}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            cash = randint(50, 500)
            print(f"Запрос на {cash}")
            if cash <= self.balance:
                self.balance -= cash
                print(f"Снятие: {cash}. Баланс: {self.balance}")
            if cash > self.balance:
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

