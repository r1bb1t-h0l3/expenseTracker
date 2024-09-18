#!/usr/bin/python3

import sys
import json

DATABASE_NAME = "expenseDB.json"
ID_KEY = "id"
NAME_KEY = "name"
AMOUNT_KEY = "amount"
EXPENSE_KEY = "allExpenses"

def generateIDFromExpense(expenses):
    currentMaxID = 0
    for e in expenses:
        id = e[ID_KEY]
        if currentMaxID < id:
            currentMaxID = id
    return currentMaxID + 1

def loadExpenses():
    try:
        with open(DATABASE_NAME, 'r') as file:
            data = json.load(file)

        return data[EXPENSE_KEY]
    except:
        return []

def saveExpenses(expenses):
    expenseRecord = {
        EXPENSE_KEY: expenses
    }
    with open(DATABASE_NAME, 'w') as file:
        json.dump(expenseRecord, file, indent=4)

def addExpense(expenses, expenseName: str, amount: int):
    newTaskID = generateIDFromExpense(expenses)
    expenses.append({
        ID_KEY: newTaskID,
        NAME_KEY: expenseName,
        AMOUNT_KEY: amount
    })
    print(f"ID: {newTaskID} | Expense: {expenseName} | Amount: EUR{amount}")


def updateExpense(expenses, expenseID: int, expenseName: str, amount: float):
    for e in expenses:
        id = e[ID_KEY]
        if id == expenseID:
            message = f"ID: {expenseID}"
            if amount is not None:
                e[AMOUNT_KEY] = amount
                message += f" | Amount: EUR{amount}"
            if len(expenseName) > 0:
                e[NAME_KEY] = expenseName
                message += f" | updated expense: \"{expenseName}\""
            print(message)
            return
    print(f"ID {expenseID} doesn't exist")


def deleteExpense(expenses):
    print("delete expense")

def viewExpense():
    print("view Expense")

    # maybe dont need 2 summaries if i can build in argument
    #for same command to show month

def viewExpenseSummary():
    print("view summary")

#def viewExpenseSummaryMonth():
    #print("view summary month")

def main():
    if len(sys.argv) <= 1:
        print("invalid arguments")
        exit(1)

    expenses = loadExpenses()
    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) == 4:
            addExpense(expenses, sys.argv[2], int(sys.argv[3]))
        else:
            print("no valid input detected")
            exit(3)

    elif action == "update":
        if len(sys.argv) >= 4:
            updateExpense(expenses,
                          int(sys.argv[2]),
                          sys.argv[3],
                          float(sys.argv[4]) if len(sys.argv) > 4 else None)
        else:
            print("no valid input detected")

    elif action == "delete":
        print("delete")

    elif action == "view":
        print("view expenses")

    elif action == "view-summary":
        print("view expense summary")

   #elif action == "view-summary-month":
    # print("view summary month")
    saveExpenses(expenses)

if __name__=="__main__":
    main()
