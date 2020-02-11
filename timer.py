import time

class TestTimer():

	def __enter__(self):
		self.start_timer = time.time()
		return self

	def timer(self):
		self.avg_timer = self.end_timer - self.start_timer
		print("Время выполнения скрипта - %.5f секунд" % self.avg_timer)

	def __exit__(self,*args):
		self.end_timer = time.time()
		return self.timer()