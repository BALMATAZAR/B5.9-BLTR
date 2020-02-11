# Импорт модулей

import sys
import os
import time

# Функция многократного запуска скприта переданного в аргументе

def trying_timer(script, trying = 1):
    for i in range (int(trying)):
        os.system(script)

# Старт таймера исполнения
        
timer_start = time.time()

# Проверка на количество переданных аргументов и запуск скрипта с заданными параметрами.

try:
	if len(sys.argv) == 2:
		print("Имя выполняемого скрипта", sys.argv[1])
		sys.argv.append("1")
		trying_timer(sys.argv[1], sys,argv[2])
	else:
		print("Имя выполняемого скрипта ", sys.argv[1])
		trying_timer(sys.argv[1], sys.argv[2])

	timer_end = time.time()

	avg_time = timer_end - timer_start

	print("Количество выполнений скрипта " + sys.argv[2])
	print("Общее время выоплнения - %.5f секунд" % avg_time)
	print("Среднее время выполнения %.5f секунд" % (avg_time / int(sys.argv[2])))
except:
	print("В аргументах не передан скрипт для выполнения!")
