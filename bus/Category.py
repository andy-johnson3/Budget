class Category:

    def __init__(self, name, budgetAmt, actualAmt):
        self.name = name
        self.budgetAmt = budgetAmt
        self.actualAmt = actualAmt

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setBudgetAmt(self, amount):
        self.budgetAmt = amount
    
    def getBudgetAmt(self):
        return self.budgetAmt
    
    def setActualAmt(self, amount):
        self.actualAmt += amount
    
    def getActualAmt(self):
        return self.actualAmt

    def __str__(self):
        return f"{self.name}\t${self.budgetAmt}\t${self.actualAmt}"