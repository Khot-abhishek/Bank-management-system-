def write_file(location, text):
    file = open('logging_info.txt', 'w')
    file.write(f'{location}: {text}') 
