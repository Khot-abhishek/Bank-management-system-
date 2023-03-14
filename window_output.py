
def window_header():     # displaying the upper box
    print('#'*80)
    print('#'+ ' '*78 +'#')
    print('#'+ 'BANK MANAGEMENT SYSTEM'.center(77,' '), '#')
    print('#'+ ' '*78 +'#')
    print('#'*80)
    print('#'+ ' '*78 +'#')

def window_footer():       # displaying the lower box border 
    print('#'+ ' '*78 +'#')
    print('#'*80)


def display_window(option_list, *args, **kwargs):
    print('args: ',args)
    print('kwargs: ',kwargs)
    window_header()  	
    if not kwargs:
        for option_text in option_list:
            print('#'+ option_text.ljust(77,' '), '#')
    else:
        for option_text, op_value in zip(option_list, kwargs.values()):
            # print('op-text: ',option_text)
            # print('op_value: ',op_value)
            option_text = option_text + ' ' + op_value
            # print('final op-text: ',option_text)
            print('#'+ option_text.ljust(77,' '), '#')

    window_footer()  	


def display_entry_window(option_list, *args, **kwargs):
    print('ent-args: ',args)
    print('ent-kwargs: ',kwargs)
    value_list = {}
    window_header()  	
    for option_text in option_list:
        print('#'+ option_text.ljust(77,' '), '#')
    window_footer()  	

    for item in args:
        title = item
        item = input(f'{item}: ')
        value_list[title] = item
    
    return value_list





################# Constants ################# 

COMMAND_OPTION_LIST = ['',
					   '  1.Check your Balance', 
		               '  2.Withdraw Amount', 
					   '  3.Deposite Amount', 
					   '  4.Account Statement', 
					   '  5.Change Your PIN'
					]

ENTRY_OPTION_LIST = [
					 '  1. LOGIN', 
		             '  2. CREATE NEW ACCOUNT'
					 ]

LOGIN_OPTION_LIST = [
					'  ENTER USERNAME: ', 
					'  YOUR PASSWORD: '
					]
LOGIN_VARS = ['EMAIL', 'PASSWORD']

SIGNUP_OPTION_LIST = [
    					' FIRST NAME: ',
                        ' LAST NAME:  ',
                        ' EMAIL:      ',
                        ' GENDER:     ',
                        ' PASSWORD:   ',
    ]
SIGNUP_VARS = ['FIRST NAME', 'LAST NAME', 'EMAIL', 'GENDER', 'PASSWORD']

BANKING_OPTIONS_LIST = [
    '  1.Withdraw Amount',
    '  2.Deposite Amount',
    '  3.Balance Enquiry',
    '  4.Account Statement',
    '  5.Change PIN'
    '  6.Log-Out'
]