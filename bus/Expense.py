# Even though it has the same attributes and methods of a Category, I didn't think it made sense, conceptually, to make it a child class because
# 1) a SubCategory is not a Category
# 2) a Categories budgetAmts and actualAmts are both calculated

class Expense():

    def __init__(self, name, category, budgetAmt, actualAmt):
        self.name = name
        self.category = category
        self.budgetAmt = budgetAmt
        self.actualAmt = actualAmt
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setCategory(self, category):
        self.category = category
    
    def getCategory(self):
        return self.category
    
    def setBudgetAmt(self, amount):
        self.budgetAmt = amount
    
    def getBudgetAmt(self):
        return self.budgetAmt
    
    def setActualAmt(self, amount):
        self.actualAmt += amount
    
    def getActualAmt(self):
        return round(self.actualAmt, 2)

    def setAttributesAsLyst(self):
        self.attributesAsLyst = [self.name, self.category, self.budgetAmt, self.actualAmt]

    def getAttributesAsLyst(self):
        self.setAttributesAsLyst()
        return self.attributesAsLyst

    def __str__(self):
        return f"{self.name}\t${self.budgetAmt}\t${self.actualAmt}"