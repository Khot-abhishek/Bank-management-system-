############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from bank_database.models import *

############################################################################
##                      START OF APPLICATION                              ##
############################################################################

from window_output import *
from feature_functions import *
from banking_operations import BankOperation
from time import sleep

# User constants
RUNNING = True
IS_AUTHENTICATED = False
bank_operation_user = None

def clear_screen():
	os.system('cls')



def main():
	global IS_AUTHENTICATED
	global bank_operation_user
	global RUNNING

	if IS_AUTHENTICATED:
		logging.info('Displaying Banking OPtions after autherization ')
		display_entry_window(BANKING_OPTIONS_LIST)
		choice = input('\nEnter your choice: ')
		if choice not in ['1','2','3','4','5','6','7']:
			print('\nWRONG INPUT, please enter the correct Choice')
			sleep(1)
			clear_screen()
		else:
			if choice == '1':
				bank_operation_user.withdraw_amount()
			elif choice == '2':
				bank_operation_user.deposite_amount()
			elif choice == '3':
				logging.info(f'CHOICE-3: bank_operation_user: {bank_operation_user}')
				bank_operation_user.show_balance()
			elif choice == '4':
				choice = bank_operation_user.show_account_statement()
				if choice:
					RUNNING = False
			elif choice == '5':
				bank_operation_user.change_pin()
			elif choice == '6':
				IS_AUTHENTICATED = False
				bank_operation_user = None
			elif choice == '7':
				RUNNING = False	
	else:
		display_window(ENTRY_OPTION_LIST)
		print()
		logging.info('Displayed the main Entry options ')
		choice = input('Enter your choice: ')
		if choice in ['1', '2']:
			selected_option = [" ", 'LOGIN', 'SIGNUP', 'WRONG_CHOICE']
			logging.info(f'User choice : {selected_option[int(choice)]}')
		else:
			logging.info(f'INVALID Choice :{choice}')
		clear_screen()
		if choice == '1':
			login_response = user_login()
			if login_response[0] == True:
				IS_AUTHENTICATED = True
				user_object = login_response[1]
				user_account = Account.objects.get(owner_id=user_object.id)
				logging.info(f"Initializing the BANK-OPERATION-obj to carryout banking \noperations for current logged-in user")
				bank_operation_user = BankOperation(user_object, user_account)
				logging.info(f'bank_operation_user: {bank_operation_user}')

		elif choice == '2':
			user_signup()
			clear_screen()
		else:
			RUNNING = False
			logging.info('Program Terminated')
			

if __name__ == '__main__':
	text = 'start of the program'.center(70, "-")
	logging.info(f"\n{text}")
	while RUNNING:
		main()
		print('running: ',RUNNING)
	else:
		text = "End of current Program Exection".center(70, "#")
		logging.info(f"{text} \n\n")