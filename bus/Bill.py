from bus.Expense import Expense

class Bill(Expense):

    def __init__(self, name, category, budgetAmt, actualAmt, dueDate, autoPay):
        super().__init__(name, category, budgetAmt, actualAmt)
        self.dueDate = dueDate
        self.autoPay = autoPay

    def setDueDate(self, dueDate):
        self.dueDate = dueDate
    
    def getDueDate(self):
        return self.dueDate
    
    def setAutoPay(self, autoPay):
        self.autoPay = autoPay
    
    def getAutoPay(self):
        return self.autoPay
    
    def setAttributesAsLyst(self):
        self.attributesAsLyst = [self.name, self.budgetAmt, self.actualAmt, self.dueDate, self.autoPay]

    def getAttributesAsLyst(self):
        self.setAttributesAsLyst()
        return self.attributesAsLyst
    
    def __str__(self):
        return f"'{self.name}','${self.budgetAmt}','${self.actualAmt}','{self.dueDate}','{self.autoPay}'"

