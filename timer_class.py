import time

class timeclock():
	def __init__(self, function):
		self.tun = function

	def timer(self, *args, trying = 1):
		self.trying = trying
		self.start_timer = time.time()
		for i in range(self.trying):
			self.run(*args)
		self.end_timer = time.time()
		self.avg_timer = self.end_timer - self.start_timer
		print("Количество выполнений скрипта {}".format(self.trying))
		print("Общее время выполнения - %.5f секунд" % self.avg_timer)
		print("Среднее время выполнения %.5f секунд" % (self.avg_timer / self.trying))