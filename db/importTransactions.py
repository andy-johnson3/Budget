import pandas as pd
import sqlalchemy
import db.db_ops
import os

# ENHANCEMENTS
#   1 - Update updateTransactionNameDB to work with pandas DF (wouldn't have to create and read the merged file, just pass the merged DF between functions)
#   2 - Update code to read transaction names and tags from the transactions table - 1 less table to maintain

def importTransactions():
    # Merge account statements
    mergeStatements()

    # Update transaction name db with current transactions
    if (updateTransactionNameDB()):
        mergedFileDF = pd.read_csv('db/MERGED_TRANSACTIONS.csv')

        # Load transaction name database into dictionary (Key:transaction name, Value: tag name)
        transDB = db.db_ops.loadTransactionNameDB()

        # Tag transactions
        for name in transDB:
            mergedFileDF.loc[mergedFileDF['Transaction_Name'] == name, ['Transaction_Tag']] = transDB.get(name)

        # SQL engine for working with database
        engine = sqlalchemy.create_engine('sqlite:///db\johnson_budget_db.db')

        # Insert into Transactions Database
        mergedFileDF.to_sql('Transactions', engine, if_exists='append', index=False)

    else:
        print('Did not import transactions.  Tag new transactions in name DB before running again.')
        os.system('pause')

def mergeStatements():
    # Edit joint account columns
    try:
        jointDF = pd.read_csv("db/USBank_Joint_Transactions.csv")
    except FileNotFoundError:
        print("'USBank_Joint_Transactions.csv' file not found.  Returning to menu.")
        return
    
    jointDF['Account'] = 'USBank_Joint'
    jointFinal = jointDF.drop(columns=['Transaction', 'Memo'])
    jointFinal['Date'] = pd.to_datetime(jointFinal.Date)
    jointFinal['Date'] = jointFinal['Date'].dt.strftime('%Y-%m-%d')

    # Edit capital one account columns
    try:
        capitalOneDF = pd.read_csv("db/andy_cc_transaction_download.csv")
    except FileNotFoundError:
        print("'andy_cc_transaction_download.csv' file not found.  Returning to menu.")
        return

    capitalOneDF['Account'] = 'Capital_One'
    capitalOneFinal = capitalOneDF[~capitalOneDF['Debit'].isnull()]\
        .drop(columns=['Posted Date', 'Card No.', 'Category', 'Credit'])\
            .rename(columns = {'Transaction Date':'Date', 'Description':'Name', 'Debit':'Amount'})

    # Merge dataframes
    mergedDF = pd.concat([jointFinal, capitalOneFinal], axis=0)

    # Rename columns
    mergedDF.rename(columns={'Date':'Transaction_Date', 'Name':'Transaction_Name', 'Amount':'Transaction_Amount', 'Account':'Transaction_Account'}, inplace=True)

    # Edit or drop specific rows 
    mergedDF.loc[mergedDF['Transaction_Name'].str.contains('Amazon Prime'), 'Transaction_Name'] = 'Amazon Prime'
    mergedDF.drop(mergedDF[mergedDF.Transaction_Name.str.contains('WEB AUTHORIZED PMT CAPITAL ONE')].index, inplace=True)

    # Create column for tag, setting each value to an empty string
    mergedDF['Transaction_Tag'] = ''

    # Create merged transaction file for tagging
    mergedDF.to_csv('db/MERGED_TRANSACTIONS.csv', index=False, header=True)


def updateTransactionNameDB():

    # Open transaction file 
    try:
        transactionsFile = open('db/MERGED_TRANSACTIONS.csv', 'r')
    except FileNotFoundError:
        print("'MERGED_TRANSACTIONS.csv' file not found.  Returning to menu.")
        return False
    else:
        transactions = transactionsFile.readlines()
        transactionsFile.close()


    # Remove header from transaction list
    transactions.pop(0)
    
    # Load transaction name database into dictionary (Key:transaction name, Value: tag name)
    transDB = db.db_ops.loadTransactionNameDB()

    # Set for transaction names that aren't in the database
    notInTransactionDB = set()

    # skipThese = ['amzn mktp', 'wal-mart', 'target', 'sams club', 'etsy.com']
    # Check if all transactions are in the database.  If not, add to the set
    for i in transactions:
        lineList = i.split(",")          
        if transDB.get(lineList[1]) == None: 
            if lineList[1].lower().__contains__('amzn mktp') or \
                lineList[1].lower().__contains__('wal-mart') or \
                lineList[1].lower().__contains__('target') or \
                lineList[1].lower().__contains__('sams club') or \
                lineList[1].lower().__contains__('etsy.com'):
                continue
            else:
                notInTransactionDB.add(lineList[1])

    # Add new transaction names to database
    if (len(notInTransactionDB)):
        os.system('cls')
        print("Number of transactions that didn't match transaction database: " + str(len(notInTransactionDB)) + "\n")
        for i in notInTransactionDB:
            print(i)
        entry = input("Enter all? (y/n)")
        if entry.lower() == 'y':
            db.db_ops.insertToTransactionNameDB(notInTransactionDB)
            os.system('cls')
            print("New Transaction Names inserted.  Open Transaction_Names table to apply a Tag!")
            os.system('pause')
            return False
        else:
            print("New transaction names were not inserted.")
            os.system('pause')
            return False
    else:
        print("All transaction names located in database")
        os.system('pause')

        return True


if __name__ == '__main__':
    mergeStatements()