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

	def calc_Ui(self):
		if self.Pass == 1:
			return -( calc_Ce1(agent.pass1) + calc_Ce3(agent.pass1) )
		elif self.Pass == 2:
			return -( calc_Ce2(agent.pass2) + calc_Ce4(agent.pass2) )
		elif self.Pass == 3:
			return -( calc_Ce1(agent.pass3) + calc_Ce4(agent.pass3) + calc_Ce5(agent.pass3) )


	def potential(self):
		value
		#e1の計算
		for k in range(1, agent.pass1 + agent.pass3 + 1):
			value += calc_Ce1(k)
		#e2の計算
		for k in range(1, agent.pass2 + 1):
			value += calc_Ce2(k)
		#e3の計算
		for k in range(1, agent.pass1 + 1):
			value += calc_Ce3(k)
		#e4の計算
		for k in range(1, agent.pass2 + agent.pass3 +1):
			value += calc_Ce4(k)
		#e5の計算
		for k in range(1, agent.pass3 + 1):
			value += calc_Ce5(k)

#エージェントの初期化
agent_list =['a', 'b', 'c', 'd']
for N in agent_list:
	agent_list = agent()
