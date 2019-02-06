#複雑システム論レポート課題
#2 (b)

class agent:
	pass1 = 0
	pass2 = 0
	pass3 = 0

	def __init__(self):
		self.Pass = 1
        agent.pass1 += 1

	def change_pass(self, newpass):
		if self.Pass == 1:
			agent.pass1 -= 1
		elif self.Pass == 2:
			agent.pass2 -= 1
		elif self.Pass == 3:
			agent.pass3 -= 1
		self.Pass = newpass

	def calc_Ce1(self, num):
		return 3+3*num

	def calc_Ce2(self, num):
		return 19+num

	def calc_Ce3(self, num):
		return 19+num

	def calc_Ce4(self, num):
		return 3+3*num

	def calc_Ce5(self, num):
		return 6+num
