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
IS_AUTHENTICATED = False


def clear_screen():
	os.system('cls')



def main():
	global IS_AUTHENTICATED

	all_operations = {

	'1': bank_operation_user.withdraw_amount,
	'2': bank_operation_user.deposite_amount,
	'3': bank_operation_user.show_balance,
	'4': bank_operation_user.show_account_statement,
	'5': bank_operation_user.change_pin,
	'6': bank_operation_user.get_user_logged_out,
	'7': bank_operation_user.end_program,
}

	
	if IS_AUTHENTICATED:
		logging.info('Displaying Banking OPtions after autherization ')
		display_entry_window(BANKING_OPTIONS_LIST)
		choice = input('\nEnter your choice: ')
		if choice not in ['1','2','3','4','5','6','7']:
			print('\nWRONG INPUT, please enter the correct Choice')
			sleep(1)
			clear_screen()
		else:
			operation = all_operations[choice]
			operation()	
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
				global bank_operation_user

		elif choice == '2':
			user_signup()
			clear_screen()
		else:
			global RUNNING
			RUNNING = False
			logging.info('Program Terminated')
			


RUNNING = True

if __name__ == '__main__':
	text = 'start of the program'.center(70, "-")
	logging.info(f"\n{text}")
	while RUNNING:
		main()
		print('running: ',RUNNING)
	else:
		text = "End of current Program Exection".center(70, "#")
		logging.info(f"{text} \n\n")