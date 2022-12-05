def check_ext(data):
    if data.endswith('xlsx'):
        print('Correct extension. Continue...')
        return True
    elif data.endswith('xls'):
        print('Correct extension. Continue...')
        return True
    else:
        print('WARNING: INCORRECT extension. Continue...')
        return False
