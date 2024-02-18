from bus.Expense import Expense

class Income(Expense):

    def __init__(self, name, category, budgetAmt, actualAmt, payRate, grossAmt):
        super().__init__(name, category, budgetAmt, actualAmt)
        self.payRate = payRate
        self.grossAmt = grossAmt
    
    def setPayRate(self, payRate):
        self.payRate = payRate
    
    def getPayRate(self):
        return self.payRate
    
    def setGrossAmt(self, grossAmt):
        self.grossAmt = grossAmt
    
    def getGrossAmt(self):
        return self.grossAmt
    
    def setAttributesAsLyst(self):
        self.attributesAsLyst = [self.name, self.budgetAmt, self.actualAmt, self.payRate, self.grossAmt]

    def getAttributesAsLyst(self):
        self.setAttributesAsLyst()
        return self.attributesAsLyst

    def __str__(self):
        return f"{self.name}\t{self.payRate}\t${self.budgetAmt}\t${self.actualAmt}\t{self.grossAmt}"