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
        return data
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

def updateExpense(expenses, expenseID: int, expenseName: str, amount: int):
    for e in expenses:
        id = e[ID_KEY]
        if id == expenseID:
            e[NAME_KEY] = expenseName
            if amount is not None:
                e[AMOUNT_KEY] = amount
            print(f"ID: {expenseID} | updated expense: {expenseName}) | Amount: {amount}")

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
        if len(sys.argv) == 4:
            updateExpense(expenses, int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        print(f"expense ID: {sys.argv[2]} successfully updated to \"{sys.argv[3]}\" with amount EUR{sys.argv[4]}")

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
