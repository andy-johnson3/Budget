import os
import db.createBudget
import db.importTransactions
from datetime import datetime
from dateutil.relativedelta import relativedelta
    
def budgetMenu(): 
    os.system('cls')
    
    print('----------BUDGET MENU-----------')
    entry = input('Import new transactions? (y/n)')
    if entry.lower() == 'y':
        db.importTransactions.importTransactions()
    else:
        print("Transactions were not imported")
        os.system('pause')

    while True:
        os.system('cls')
        displayMenu()

        today = datetime.now()

        entry = input("Make a selection:")
        if entry == '1':
            month = today.strftime('%m')
            year = today.strftime('%Y')
            budget = db.createBudget.createBudget(month, year)
            print(budget)
            os.system('pause')
        elif entry == '2':
            lastMonth = today - relativedelta(months = 1)
            month = lastMonth.strftime('%m')
            year = lastMonth.strftime('%Y')
            budget = db.createBudget.createBudget(month, year)
            print(budget)
            os.system('pause')
        elif entry == '3':
            month = input("Enter a month in XX format: ")
            year = input("Enter a year in XXXX format: ")
            budget = db.createBudget.createBudget(month, year)
            print(budget)
            os.system('pause')
        elif entry == '4':
            pass
        elif entry == '5':
            pass
        elif entry == '6':
            pass
        elif entry == '7':
            pass
        elif entry == '8':
            pass
        elif entry == '9':
            pass
        elif entry == '0':
            break
        else:
            os.system('cls')
            print("\n****** ERROR: Invalid Selection. Please try again. ******\n")

    print("Ope, Bye!")

def displayMenu():
    print('----------BUDGET MENU-----------')
    print("1.  View Budget - This Month")
    print("2.  View Budget - Last Month")
    print("3.  View Budget - Custom Date Range")
    print("4.  ")
    print("5.  ")
    print("6.  ")
    print("7.  ")
    print("8.  ")
    print("9.  ")
    print("\nEXIT")
    print("-----")
    print("0.  Exit\n")

if __name__ == '__main__':
    budgetMenu()