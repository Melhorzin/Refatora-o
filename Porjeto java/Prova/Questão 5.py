import os.path
import csv
from datetime import datetime

def save_expense(expense, filename):
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(expense)

def load_expenses(filename):
    expenses = []
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
    return expenses

def get_current_month():
    now = datetime.now()
    return (now.strftime('%m'), now.strftime('%Y'))

def get_expenses_for_month(expenses, month, year):
    expenses_for_month = []
    for expense in expenses:
        if expense[2] == month and expense[3] == year:
            expenses_for_month.append(expense)
    return expenses_for_month

def calculate_balance(expenses, income):
    total_expenses = 0
    for expense in expenses:
        total_expenses += float(expense[1])
    balance = income - total_expenses
    return balance

def main():
    filename = 'expenses.csv'
    income = float(input('Digite o valor do seu rendimento mensal: '))
    while True:
        print('\n--- MENU ---')
        print('1. Consultar despesas')
        print('2. Consultar saldo do mês atual')
        print('3. Consultar saldo de um mês específico')
        print('4. Informar renda')
        print('5. Informar despesa')
        print('0. Sair')
        option = input('Digite a opção desejada: ')
        if option == '1':
            expenses = load_expenses(filename)
            for expense in expenses:
                print(expense)
        elif option == '2':
            expenses = load_expenses(filename)
            month, year = get_current_month()
            expenses_for_month = get_expenses_for_month(expenses, month, year)
            balance = calculate_balance(expenses_for_month, income)
            print(f'Saldo atual: R${balance:.2f}')
        elif option == '3':
            expenses = load_expenses(filename)
            month = input('Digite o mês (MM): ')
            year = input('Digite o ano (AAAA): ')
            expenses_for_month = get_expenses_for_month(expenses, month, year)
            balance = calculate_balance(expenses_for_month, income)
            print(f'Saldo de {month}/{year}: R${balance:.2f}')
        elif option == '4':
            income = float(input('Digite o valor da sua renda mensal: '))
            print('Renda atualizada com sucesso!')
        elif option == '5':
            expenses = load_expenses(filename)
            expense_value = input('Digite o valor da despesa: ')
            expense_month, expense_year = get_current_month()
            expense_description = input('Digite a descrição da despesa: ')
            expense = [expense_value, expense_description, expense_month, expense_year]
            try:
                balance = calculate_balance(expenses, income)
                if float(expense_value) > balance:
                    print('Saldo insuficiente para realizar essa despesa!')
                else:
                    save_expense(expense, filename)
                    print('Despesa salva com sucesso!')
            except ValueError:
                print('Valor da despesa inválido!')
        elif option == '0':
