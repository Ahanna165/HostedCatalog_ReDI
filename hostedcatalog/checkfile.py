def check_ext(data):
    if data.endswith('xlsx'):
        print('Correct extension. Uploading...')
        return True
    elif data.endswith('xls'):
        print('Correct extension. Uploating...')
        return True
    else:
        print('Non-excel. Continue with default...')
        return False


