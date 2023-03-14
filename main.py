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
from time import sleep


Current_User_details = {}
USER_LOGGED_IN = False

def clear_screen():
	os.system('cls')
	

def main():
	if USER_LOGGED_IN:
		pass
	else:
		display_window(ENTRY_OPTION_LIST)
		print()
		choice = input('Enter your choice: ')
		clear_screen()
		if choice == '1':
			pass
		elif choice == '2':
			pass
		else:
			global RUNNING
			RUNNING = False
			print('turned off')
			


RUNNING = True

if __name__ == '__main__':
	
	while RUNNING:
		main()
		print('running: ',RUNNING)