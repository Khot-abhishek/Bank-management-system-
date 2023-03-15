from window_output import *
from time import sleep
import random
import os
from bank_database.models import User, Account

import logging
logging.basicConfig(filename='BMS_logs.log', level=logging.INFO)




def clear_screen():
	os.system('cls')


def loading_animation(title = None, speed=0.2):
	"""
	a simple loading bar animation where ,title = for which operation
	the animation is for (LOGIN, Creating New Account,etc)
	"""
	logging.info(f"Showing The loading animation for : {title}")
	if title == None:
		title = 'Loading'
	for i in range(1,25):       # animated progress bar
		loading_bar = '#'* i
		loading_bar = loading_bar.ljust(25,'.')
		print(f'{title} [' + loading_bar + ']')
		sleep(speed)
		clear_screen()


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
		print("(TYPE--> 'Y,y' = create account, 'N,n' = Re-enter details , 'Q,q' to quit)\n")
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
			response = create_new_account(signup_vals)
			logging.info(f'create_new_account-response : {response}')
			if response is not None:
				if response[0] == 'Created':

					loading_animation('Creating Your Account')
					print(f'{response[1]} : Your Account was successfully created..')
					sleep(3)
					clear_screen()
					print('Login Using you EMAIL & PASSWORD..\n')
					user_login()
			else:
				clear_screen()
				print('Something went wrong with your credentials , Please Enter proper Details.')
				user_signup()
	return response[1]

	


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
		return ['Created', f_name] 
	else:
		logging.ERROR('Something went wrong with either User created or his retrievel after creation')
		return 
	
def user_login():
	logging.info('showing login Window to user')
	login_vals = display_entry_window(LOGIN_OPTION_LIST, *LOGIN_VARS)
	logging.info(f'User login credentials: {login_vals}')
	clear_screen()
	display_window(LOGIN_OPTION_LIST, **login_vals)
	print("(TYPE-->  'Y|y' to LOGIN,  'N|n' to re-enter info)\n")
	choice = input('>>> : ')
	if choice == 'n' or choice == 'N':
		logging.info('User choose to re-enter login info')
		clear_screen()
		print('Re-Enter your details')
		user_login()
	elif choice == 'y' or choice == 'Y':
		logging.info('User waitung for login authentication')
		loading_animation('Logging In')
		username, password = list( login_vals.values() )
		is_authenticated, user_object = authenticate_user(username, password)
		if is_authenticated:
			return (is_authenticated, user_object[0])  # since it's a list of dict ,returning the Dict as individual obj
		else:
			display_remark_box('Wrong Username or Password, please enter corrent info')
			user_login()
	else:
		clear_screen()
	return [False, '']

def authenticate_user(username, password):
	logging.info(f'authenticate: getting user from database: {username}-{password} ')
	current_user = User.objects.filter(email=username, password=password).values()
	logging.info(f"query returned: current user = {current_user}")
	if current_user:
		return [True, list( current_user )]   # returning as a 'list' instead of 'QuerySet'
	return [False, '']


def initialize_bank_account_for_user(email, password):
	logging.info('initialixing bank account')
	owner = User.objects.get(email=email, password=password)
	owner_id = owner.id
	account_number = random.randrange(863298216, 4863298216)
	new_account = Account(owner=owner, account_type='Savings', account_number = account_number, balance = 0.0)
	new_account.save()


