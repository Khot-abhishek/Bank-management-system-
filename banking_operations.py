from bank_database.models import User, Account, Statement
from window_output import *
import os
RUNNING = True


class BankOperation:

    def __init__(self, current_user, user_account):
        self.current_user = current_user
        self.user_account = user_account

    def __str__(self):
        return  f'Bank Operations For : {self.current_user.f_name}'
    
    def deposite_amount(self):
        logging.info('Entered deposite_amount FUNCTION')
        text = 'Enter the Deposite amount'
        display_operations_window(text)
        amount = input('Enter amount: ')
        logging.info(f'Entered deposite_amount : {amount}')
        old_bal = self.user_account.balance
        new_bal = float(old_bal) + float(amount)
        self.user_account.balance = new_bal
        self.user_account.save()
        statement = Statement(description='APP Withdraw', debited=0.0, created=amount, balance=new_bal, st_owner_id=self.user_account.id)
        statement.save()
        logging.info('Created a statement for tte current (deposite) transaction')
        self.show_balance()


    def withdraw_amount(self):
        logging.info('Entered withdraw_amount FUNCTION')
        text = 'Enter the withdraw amount amount'
        display_operations_window(text)
        amount = input('Enter amount: ')
        logging.info(f'Entered withdraw_amount : {amount}')
        old_bal = self.user_account.balance
        new_bal = float(old_bal) - float(amount)
        self.user_account.balance = new_bal
        self.user_account.save()
        statement = Statement(description='APP Withdraw', debited=amount, created=0.0, balance=new_bal, st_owner_id=self.user_account.id)
        statement.save()
        logging.info('Created a statement for tte current (withdraw) transaction')
        self.show_balance()

    def show_balance(self):
        logging.info('Entered show_balance--')
        balance = self.user_account.balance
        text = f'Current Account Balance:  Rs.{balance}'.center(78)
        display_operations_window(text)
        choice = input('Your Choice : ')
        if choice == '2':
            global RUNNING
            RUNNING = False           
            

    def change_pin(self):
        pass

    def show_account_statement(self):
        statements = Statement.objects.filter(st_owner_id=self.user_account.id).values()
        display_statements(*statements)
        os.system('cls')
        print('\nEnter  1.Go to Main window      2.Quit')
        choice = input('Enter : ')
        if choice == '2':
            return True