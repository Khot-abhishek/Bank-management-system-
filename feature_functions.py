from window_output import *
from time import sleep
import os
from logging_12 import write_file
from bank_database.models import User


def clear_screen():
	os.system('cls')

def user_signup():
	location = 'user_signup'
	signup_vals = display_entry_window(SIGNUP_OPTION_LIST, *SIGNUP_VARS)
	print('sign vals: ',signup_vals)
	clear_screen()
	display_window(SIGNUP_OPTION_LIST, **signup_vals)
	correct_option = False
	while not correct_option:
		print("(TYPE--> 'Y,y' = create account, 'N,n' = Re-enter details , 'Q,q' to quit)")
		choice = input('>> :')
		print('your choice :',choice)

		if choice == 'q' or choice == 'Q':
			correct_option = True
			global Running
			Running = False

		elif choice == 'n' or choice == 'N':
			correct_option = True
			clear_screen()
			user_signup()
		elif choice == 'y' or choice == 'Y':
			correct_option = True
			print('signup values : ',signup_vals)
			write_file(location, signup_vals)
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
	location = 'create_new_account'
	info_list = list( account_details.values() )
	write_file(location, info_list)
	f_name,m_name,l_name,email,gender,password = info_list
	text=''
	for val in info_list:
		text += val
	write_file(location, text)
	print(f'{f_name}, {m_name}, {l_name}, {email}, {gender}, {password}')
	sleep(3)
	new_user = User(f_name=f_name, m_name=m_name, l_name=l_name, email=email, gender=gender, password=password)
	new_user.save()
	qs = User.objects.filter(f_name=f_name)
	print('Quesryset: ',qs)
	sleep(3)
	return ['created', f_name] 
