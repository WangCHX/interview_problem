class Flatten:
	def __init__(self, nums):
		self.nums = nums
		self.current_x = 0
		self.current_y = 0
		
	def has_next(self):
		return self.current_x < len(self.nums)
		
	def next(self):
		if self.has_next():
			res = self.nums[self.current_x][self.current_y]
			self.current_y += 1
			if self.current_y >= len(self.nums[self.current_x]):
				self.current_y = 0
				self.current_x += 1
			return res
		return -1
		
		
		
		
x = Flatten([[1, 2],[3, 4, 5]])
while x.has_next():
	print x.next()