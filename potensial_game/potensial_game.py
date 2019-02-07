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
		if newpass == 1:
			agent.pass1 += 1
		elif newpass == 2:
			agent.pass2 += 1
		elif newpass == 3:
			agent.pass3 +=1

	def print_pass(self):
		print("pass1:", agent.pass1, ", pass2:", agent.pass2, ", pass3:", agent.pass3)

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
			return -( self.calc_Ce1(agent.pass1) + self.calc_Ce3(agent.pass1) )
		elif self.Pass == 2:
			return -( self.calc_Ce2(agent.pass2) + self.calc_Ce4(agent.pass2) )
		elif self.Pass == 3:
			return -( self.calc_Ce1(agent.pass3) + self.calc_Ce4(agent.pass3) + self.calc_Ce5(agent.pass3) )

	def calc_objfunc(self):
		ans = 0
		for i in range(agent.pass1 + agent.pass2 + agent.pass3):
			for j in range(agent.pass1):
				ans += -( self.calc_Ce1(agent.pass1) + self.calc_Ce3(agent.pass1) )
			for j in range(agent.pass2):
				ans += -( self.calc_Ce2(agent.pass2) + self.calc_Ce4(agent.pass2) )
			for j in range(agent.pass3):
				ans += -( self.calc_Ce1(agent.pass3) + self.calc_Ce4(agent.pass3) + self.calc_Ce5(agent.pass3) )
		return ans
			


	def potential(self):
		value = 0
		#e1の計算
		for k in range(1, agent.pass1 + agent.pass3 + 1):
			value += self.calc_Ce1(k)
		#e2の計算
		for k in range(1, agent.pass2 + 1):
			value += self.calc_Ce2(k)
		#e3の計算
		for k in range(1, agent.pass1 + 1):
			value += self.calc_Ce3(k)
		#e4の計算
		for k in range(1, agent.pass2 + agent.pass3 +1):
			value += self.calc_Ce4(k)
		#e5の計算
		for k in range(1, agent.pass3 + 1):
			value += self.calc_Ce5(k)
		return -value

#エージェントの初期化
agent_list=[agent(), agent(), agent(), agent()]

for i, name in enumerate(agent_list):
	print("エージェント", i,"の移動")
	for j in range(3):
		name.print_pass()
		#print("効用関数：", name.calc_Ui())
		#print("ポテンシャル関数：", name.potential())
		#print("大域目的関数：", name.calc_objfunc())
		if j ==0:
			name.change_pass(2)
		elif j == 1:
			name.change_pass(3)