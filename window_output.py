import logging


def window_header(remark=None):     # displaying the upper box
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
    logging.info(f"DISP_WINDOW- args: {args} | kwargs: {kwargs} ")
    window_header()  	
    if not kwargs:
        for option_text in option_list:
            print('#'+ option_text.ljust(77,' '), '#')
    else:
        for option_text, op_value in zip(option_list, kwargs.values()):
            option_text = option_text + ' ' + op_value
            print('#'+ option_text.ljust(77,' '), '#')

    window_footer()  	


def display_entry_window(option_list, *args, **kwargs):
    logging.info(f"ENT--DISP_WINDOW- args: {args} | kwargs: {kwargs} ")
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


def display_remark_box(remark):
    print('"'*80)
    print(remark.center(80, ' '))
    print('"'*80)


def display_operations_window(text=None):
    output_options = ['  1.Go to Main Window', '  2.Quit'] 
    window_header()
    if text:
        print('#'+ text.ljust(77,' ') + '#')
        print('#'+ '-'.center(77, '-') + '#')
    print('#'+ ' '*78 +'#')
    print('#'+ ' '*78 +'#')
    for option in output_options:
        print('#'+ option.ljust(77,' ') + '#')
    window_footer()

def display_statements(*all_statements):
    # 10-10-25-10-10-15
    print('#'*97)
    print('#' + 'Sl.no'.center(10) + '|' + 'ID'.center(10) +'|' + 'Date'.center(10) + '|' + 'Description'.center(25) + '|' + 'Debited'.center(10) + '|' + 'Credited'.center(10) + '|' + 'Balance'.center(15) + '#')
    print('#'*97)
    print('#' + ' '.center(85) + '#')

    main_list = []
    spacing = [10,10,10,25,10,10,15]
    for record in all_statements:
        logging.info(f'record: {record}')
        record_vals = record.values()
        logging.info(f'record-vals: {record_vals}')

        list = []
        for val,spac in zip(record_vals, spacing):
            val = str(val)
            text = val.center(spac)
            list.append(text)
        text = '|'.join(list)
        text = '|' + text + '|'
        print(text)
        print('-'*97)
    print('#'*97)
    


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
    					' FIRST NAME:  ',
                        ' MIDDLE NAME: ',
                        ' LAST NAME:   ',
                        ' EMAIL:       ',
                        ' GENDER:      ',
                        ' PASSWORD:    ',
    ]
SIGNUP_VARS = ['FIRST NAME', 'MIDDLE NAME:','LAST NAME', 'EMAIL', 'GENDER', 'PASSWORD']

BANKING_OPTIONS_LIST = [
    '  1.Withdraw Amount',
    '  2.Deposite Amount',
    '  3.Balance Enquiry',
    '  4.Account Statement',
    '  5.Change PIN',
    '  6.Log-Out',
    '  7.QUIT'
]