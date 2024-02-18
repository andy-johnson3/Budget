class Budget:

    def __init__(self, budget_name, income, bills, subCategories):
        self.budget_name = budget_name
        self.income = income
        self.bills = bills
        self.subCategories = subCategories

    def setBudgetName(self, budget_name):
        self.budget_name = budget_name

    def getBudgetName(self):
        return self.budget_name
    
    def setIncome(self, income):
        self.income = income

    def getIncome(self):
        return self.income
    
    def setBills(self, bills):
        self.bills = bills

    def getBills(self):
        return self.bills

    def setSubCategories(self, subCategories):
        self.subCategories = subCategories

    def getSubCategories(self):
        return self.subCategories

    def __str__(self):
        toString = "-----------------------\n"
        toString += self.getBudgetName()
        toString += "\n----------------------\n"
        toString += "\nIncome\n"
        for i in self.income:
            toString += str(i) + "\n"
        toString += "\nBills\n"
        for i in self.bills:
            toString += str(i) + "\n"
        toString += "\nSubCategories\n"
        for i in self.subCategories:
            toString += str(i) + "\n"

        return toString




