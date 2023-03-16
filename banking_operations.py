from bank_database.models import User, Account, Statement
from window_output import *


class BankOperation:

    def __init__(self, current_user, user_account):
        self.current_user = current_user
        self.user_account = user_account
    
    def deposite_amount(self):
        pass

    def withdraw_amount(self):
        pass

    def show_balance(self):
        balance = self.user_account.balance
        text = f'Current Account Balance:  {balance}'.center(78)
        display_operations_window(text)
        choice = input('Your Choice : ')
        if choice

    def change_pin(self):
        pass

    def show_account_statement(self):
        pass
    
    def get_user_logged_out(self):
        pass

    def end_program(self):
        pass
