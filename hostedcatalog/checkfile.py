def check_ext(data):
    if data.endswith('xlsx'):
        print('Correct extension.')
        return True
    elif data.endswith('xls'):
        print('Correct extension.')
        return True
    else:
        print('Non-excel.')
        return False


