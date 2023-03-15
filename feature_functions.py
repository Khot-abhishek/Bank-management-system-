from window_output import *
from time import sleep
import os
from bank_database.models import User

import logging
logging.basicConfig(filename='BMS_logs.log', level=logging.INFO)


def clear_screen():
	os.system('cls')

def user_signup():
	location = 'user_signup'
	logging.info('Enter the Signup Function')
	signup_vals = display_entry_window(SIGNUP_OPTION_LIST, *SIGNUP_VARS)
	logging.info(f'Details by User: {signup_vals}')
	clear_screen()
	display_window(SIGNUP_OPTION_LIST, **signup_vals)
	logging.info('What to do with the User credentials? : ')
	correct_option = False
	while not correct_option:
		print("(TYPE--> 'Y,y' = create account, 'N,n' = Re-enter details , 'Q,q' to quit)")
		choice = input('>> :')
		print('your choice :',choice)

		if choice == 'q' or choice == 'Q':
			logging.info('User chose to quit the Program')
			correct_option = True
			global Running
			Running = False

		elif choice == 'n' or choice == 'N':
			logging.info('User choose to re-enter the details')
			correct_option = True
			clear_screen()
			user_signup()
		elif choice == 'y' or choice == 'Y':
			logging.info('User choose to signup with his given credentials')
			logging.info(f'User-credentials: {signup_vals}')
			
			correct_option = True
			sleep(4)
			responce = create_new_account(signup_vals)

			if responce is not None:
				if responce[0] == 'Created':
					print(f'{responce[1]} : Your Account was successfully created..')
					sleep(3)
					clear_screen()
					print('Login Using you EMAIL & PASSWORD..\n')
					# user_login()
			else:
				clear_screen()
				print('Something went wrong with your credentials , Please Enter proper Details.')
				user_signup()

	


def create_new_account(account_details):
	logging.info('Entered  create_new_account Function')
	info_list = list( account_details.values() )
	logging.info(f"values to create: {info_list}")
	f_name,m_name,l_name,email,gender,password = info_list
	sleep(3)
	new_user = User(f_name=f_name, m_name=m_name, l_name=l_name, email=email, gender=gender, password=password)
	new_user.save()
	qs = User.objects.filter(f_name=f_name)
	if qs:
		logging.info(f'NEW USER CREATED: {qs}')
		sleep(3)
		return ['created', f_name] 
	else:
		logging.ERROR('Something went wrong with either User created or his retrievel after creation')
		return 