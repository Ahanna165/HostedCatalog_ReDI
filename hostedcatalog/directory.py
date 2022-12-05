import os
from datetime import datetime
import xlsxwriter
import pandas as pd



class Directory:
    """Class Directory takes desired file name, month and year, desired parent directory
    and creates a folder for new catalog version"""

    def __init__(self):  # creates instance and name(name+month+year)
        self.filename = "{fileprefix}_{month} {year}".format(fileprefix=str(input('Insert catalog file prefix: ')),
                                                             year=datetime.now().strftime("%Y"),
                                                             month=str.upper(datetime.now().strftime("%b")))
        print('Instance directory created', self.filename)

    def set_directory(self):  # sets new directory with file name, checkes if there is directory
        print('Your current working directory is: ', os.getcwd())
        while True:
            parent_dir = str(input('Insert your new catalog folder destination path\nor hit enter to stay in current directory: '))
            self.dir_path = os.path.join(parent_dir, self.filename)
            isExist = os.path.exists(self.dir_path)
            if not isExist:
                try:
                    os.makedirs(self.dir_path)
                    print("Directory '%s' created" % self.dir_path)
                    break
                except FileNotFoundError:
                    print('Check connection to ', parent_dir)
                except NameError:
                    print('Check the spelling for', parent_dir)
            else:
                print("Directory '%s' exists" % self.dir_path)
                break

    def __call__(self, file): # instance = method to save a file under itself
        file.to_excel(f"{self.dir_path}\{self.filename}.xlsx",
                      sheet_name='Sheet1',
                      na_rep='',
                      index=False,
                      engine='xlsxwriter')
        print('Hosted catalog file {} saved under {}'.format(self.filename, self.dir_path))

if __name__ == '__main__':
    new_folder = Directory()
    Directory.set_directory(new_folder)
    new_folder(file)