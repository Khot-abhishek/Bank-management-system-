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
from time import sleep

# User constants
USER_PROFILE = {}
IS_AUTHENTICATED = False


def clear_screen():
	os.system('cls')
	

def main():
	global IS_AUTHENTICATED
	
	if IS_AUTHENTICATED:
		logging.info('Displaying Banking OPtions after autherization ')
		display_entry_window(BANKING_OPTIONS_LIST)
		choice = input('\nEnter your choice: ')
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