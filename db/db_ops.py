import sqlite3
from bus.Bill import Bill
from bus.Income import Income
from bus.Expense import Expense

def getConnection():
    return sqlite3.connect('db/johnson_budget_db.db')

def loadTransactions(month, year):
    print("Loading transactions...")
    conn = getConnection()
    c = conn.cursor()
    
    c.execute(f"""SELECT Transaction_Name, Transaction_Amount, Transaction_Account, Transaction_Tag 
                    FROM Transactions 
                    WHERE Transaction_Date 
                    LIKE '%{year}-{month}%';""")
    
    selection = c.fetchall()

    # transactionList = []

    # for i in selection:
    #     transactionList.append(i)

    conn.close()

    return selection

def loadTransactionNameDB():
    print("Loading transaction database...")
    conn = getConnection()
    c = conn.cursor()
    
    # Returns [('DEBIT PURCHASE -VISA CULVERS EAU CLAIEAU CLAIRE  WI', 'Restaurants'), ...... ]
    c.execute("SELECT Transaction_Name, Transaction_Tag FROM Transaction_Names")
    selection = c.fetchall()
    
    transDB = dict()

    for i in selection:
        transDB[i[0]] = i[1]

    conn.close()

    return transDB

def loadBills():

    print("Loading Bills...")
    conn = getConnection()
    c = conn.cursor()

    c.execute("""SELECT Tags.Tag_Name, Tags.Tag_Category, Tags.Tag_Budgeted_Amount, Tags.Tag_Actual_Amount, Bills_Additional.Bill_DayDue, Bills_Additional.Bill_AutoPay
                    FROM Tags
                    INNER JOIN Bills_Additional
                    ON Tags.Tag_Name = Bills_Additional.Bill_Tag;""")
    selection = c.fetchall()

    bills = []

    for i in selection:
        bills.append(Bill(i[0], i[1], i[2], i[3], i[4], i[5]))

    conn.close()

    return bills

def loadIncome():

    print("Loading Income...")
    conn = getConnection()
    c = conn.cursor()

    c.execute("""SELECT Tags.Tag_Name, Tags.Tag_Category, Tags.Tag_Budgeted_Amount, Tags.Tag_Actual_Amount, Income_Additional.Income_Rate, Income_Additional.Income_Gross_Amount
                    FROM Tags
                    INNER JOIN Income_Additional
                    ON Tags.Tag_Name = Income_Additional.Income_Tag;""")
    selection = c.fetchall()

    income = []

    for i in selection:
        income.append(Income(i[0], i[1], i[2], i[3], i[4], i[5]))

    conn.close()

    return income

def loadExpenses():

    print("Loading Expenses...")
    conn = getConnection()
    c = conn.cursor()
    
    c.execute("""SELECT Tag_Name, Tag_Category, Tag_Budgeted_Amount, Tag_Actual_Amount 
                    FROM Tags
                    WHERE NOT Tag_Category = "Income" AND NOT Tag_Category = "Bills"
                    ORDER BY Tag_Category ASC;""")
    selection = c.fetchall()

    expenses = []

    for i in selection:
        expenses.append(Expense(i[0], i[1], i[2], i[3]))

    conn.close()

    return expenses


def insertToTransactionNameDB(insert):
    print("Updating Transaction Database...")
    conn = getConnection()
    
    c = conn.cursor()
    try:
        for i in insert:
            c.execute("INSERT INTO Transaction_Names (Transaction_Name) VALUES (?)", (i,))
    except sqlite3.IntegrityError:
        print("One or more of those transaction names already exist.  Insert cancelled.")
    conn.commit()

    conn.close()

if __name__ == '__main__':
    loadIncome()

