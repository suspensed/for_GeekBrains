class Worker:
	def __init__(self, name, surename, position, wage, bonus):
		self.name = name
		self.surename = surename
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
	def __init__(self, name, surename, position, wage, bonus):
		super().__init__(name, surename, position, wage, bonus)

	def get_full_name(self):
		return self.name + ' ' + self.surename 

	def get_total_income(self):
		return f'{sum(self._income.values())}'


var = Position('Kostya', 'Kartovenko', 'HR', 45000, 33000)

print(var.get_full_name())
print(var.position)
print(var.get_total_income())