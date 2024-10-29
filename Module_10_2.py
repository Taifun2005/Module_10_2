"""
import threading
import  time

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay
    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1
    def run(self):
        print(f'Поток {self.name} запущен \n')
        self.timer(self.name,self.counter, self.delay)
        print(f'Поток {self.name} Завершон \n')

thread1 = MyThread('thread1', 5, 1)
thread2 = MyThread('thread2', 3, 0.5)
thread1.start()
thread2.start()


"""
import threading
import  time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} , на нас напали! \n')
        power_100 = 100
        day = 0
        while power_100:
            power_100 -= self.power
            day += 1
            time.sleep(0.3)
            print(f"{self.name} сражается {day}..., осталось {power_100} воинов. \n")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")




# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
# first_knight.join()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
