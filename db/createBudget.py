import os
import db.db_ops
import bus.Budget
import db.db_ops

def createBudget(month, year):

    # Load transactions with supplied month and year
    transactions = db.db_ops.loadTransactions(month, year)

    # Load budget databases into lists
    bills = db.db_ops.loadBills()
    income = db.db_ops.loadIncome()
    expenses = db.db_ops.loadExpenses()

    # Increment bill/income/expense actualAmt attributes
    for i in transactions:
        is_looping = True        
        for e in expenses:
            if i[3] == e.getName():
                e.setActualAmt(float(i[1]))
                is_looping = False
                break
        if not is_looping:
            continue
        for b in bills:
            if i[3] == b.getName():
                b.setActualAmt(float(i[1]))
                is_looping = False
                break
        if not is_looping:
            continue
        for inc in income:
            if i[3] == inc.getName():
                inc.setActualAmt(float(i[1]))
                break

    # Create the Budget
    budget = bus.Budget.Budget("Johnson Budget", income, bills, expenses)

    print("Budget created")
    os.system('pause')        
    os.system('cls')

    return budget


if __name__ == '__main__':
    createBudget()