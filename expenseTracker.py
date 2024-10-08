#!/usr/bin/python3

import sys
import json

DATABASE_NAME = "expenseDB.json"
ID_KEY = "id"
NAME_KEY = "name"
AMOUNT_KEY = "amount"
MONTH_KEY = "month"
EXPENSE_KEY = "allExpenses"

def printMonth(month: int) -> str:
    allMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return allMonths[month-1]


def generateIDFromExpense(expenses: [dict]) -> int:
    currentMaxID = 0
    for e in expenses:
        id = e[ID_KEY]
        if currentMaxID < id:
            currentMaxID = id
    return currentMaxID + 1


def loadExpenses() -> [dict]:
    try:
        with open(DATABASE_NAME, 'r') as file:
            data = json.load(file)

        return data[EXPENSE_KEY]
    except:
        return []


def saveExpenses(expenses: [dict]) -> None:
    expenseRecord = {
        EXPENSE_KEY: expenses
    }
    with open(DATABASE_NAME, 'w') as file:
        json.dump(expenseRecord, file, indent=4)

def addExpense(expenses: [dict], expenseName: str, amount: int, month: int) -> None:
    newTaskID = generateIDFromExpense(expenses)
    expenses.append({
        ID_KEY: newTaskID,
        NAME_KEY: expenseName,
        AMOUNT_KEY: amount,
        MONTH_KEY: month
    })
    print(f"ID: {newTaskID} | Expense: {expenseName} | Amount: EUR{amount} | Month: {month}")


def updateExpense(expenses: [dict], expenseID: int, expenseName: str, amount: float, month: int) -> None:
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
            if len(month) > 0:
                e[MONTH_KEY] = month
                message += f" | updated month: \"{month}"
            print(message)
            return
    print(f"ID {expenseID} doesn't exist")


def deleteExpense(expenses: [dict], expenseID: int) -> None:
    i = 0
    while i < len(expenses):
        print(f"i: {i}")
        expense = expenses[i]
        id = expense[ID_KEY]
        print(f"id: {id}")
        if id == expenseID:
            expenses.pop(i)
            print(f"expense {expenseID} successfully deleted.")
            return
        else:
            i += 1
    print(f"Current ID {expenseID} doesn't exist")

def viewExpense(expenses: [dict]) -> None:
    for expense in expenses:
        print(f"ExpenseID: {expense[ID_KEY]}")
        print(f"Expense: {expense[NAME_KEY]}")
        print(f"Amount: {expense[AMOUNT_KEY]}")
        print(f"Month: {printMonth(expense[MONTH_KEY])}")
        print('-'*20)

def viewExpenseSummary(expenses: [dict]) -> None:
    sum = 0
    for e in expenses:
        sum += e[AMOUNT_KEY]
    print(f"total expenses are EUR{sum}.")


def viewExpenseSummaryMonth(expenses: [dict], userMonth: int) -> None:
    sum = 0
    for e in expenses:
        m = e[MONTH_KEY]
        if m == userMonth:
            sum += e[AMOUNT_KEY]
    print(f"For {printMonth(userMonth)} total expenses were EUR{sum}. ")



def main():
    if len(sys.argv) <= 1:
        print("invalid arguments")
        exit(1)

    expenses = loadExpenses()
    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) == 5:
            addExpense(expenses, sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        else:
            print("no valid input detected")
            exit(3)

    elif action == "update":
        if len(sys.argv) >= 4:
            updateExpense(expenses,
                          int(sys.argv[2]),
                          sys.argv[3],
                          float(sys.argv[4]) if len(sys.argv) > 4 else None,
                          int(sys.argv[5]) if len(sys.argv) > 5 else None)
        else:
            print("no valid input detected")

    elif action == "delete":
        if len (sys.argv) == 3:
            deleteExpense(expenses, int(sys.argv[2]))
        else:
            print("no valid input detected")
            exit(4)
    elif action == "view":
        if len (sys.argv) == 2:
            viewExpense(expenses)
        else:
            print("unknown action")
        exit(2)

    elif action == "view-summary":
        if len(sys.argv) == 2:
            viewExpenseSummary(expenses)

    elif action == "view-summary-month":
        if len(sys.argv) == 3:
            viewExpenseSummaryMonth(expenses, int(sys.argv[2]))

    saveExpenses(expenses)

if __name__=="__main__":
    main()
