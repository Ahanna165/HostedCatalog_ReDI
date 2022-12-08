import logging
from time import sleep
import pandas as pd
from hostedcatalog.directory import Directory
from test_checkfile import test_check_bad_ext, test_check_2good_ext, test_check_1good_ext


logging.basicConfig(filename="program.log",
                    level=logging.DEBUG,
                    style="{",
                    format="{asctime} [{levelname:8}{module:8}{lineno:8}] {message}",
                    datefmt="%d.%m.%Y")
logging.debug('Check the workflow')
logging.info('This is information')
logging.warning('This is warning')
logging.error('Error here')
logging.critical('Critical process')

# create new folder for new catalog version or use current directory
new_folder = Directory()
Directory.set_directory(new_folder)

# import your data from .xlsx or .xls file
from hostedcatalog import inputdata, outputdata

# use test_input.xls for testing
while True:
    try:
        data = str(input('\nPATH of your INPUT file as EXCEL: ')).replace('"', '')
        if data.endswith('xlsx'):
            df = pd.read_excel(data, engine='openpyxl')
            print('File format is .xlsx', df.head())
            inputfile = inputdata.InputFile(df)
            break
        elif data.endswith('xls'):
            df = pd.read_excel(data, engine='xlrd')
            print('File format is .xls', df.head())
            inputfile = inputdata.InputFile(df)
            break
        else:
            print('File format is invalid! \nPaste the file path as .xlsx or .xls! ')
            continue
    except FileNotFoundError:
        print('FileNotFoundError!\nCheck file name before extension .xxx!')

# clean and manipulate data
inputfile = inputfile[inputfile['VOLUMEPRICE'] != 0]
print('VOLUMEPRICE selected')
inputfile = inputfile[inputfile['QTYAMOUNT'] == 1]
print('Quantity amount selected')
inputfile = inputfile.drop_duplicates(subset=['PARTNUM'])
print('Duplicates removed')
inputfile = inputdata.InputFile.set_unit(inputfile)
print('ISO Units set')
inputfile = inputdata.InputFile.sup(inputfile)
print('Special characters replaced')
inputfile = inputdata.InputFile.impute_na(inputfile)
print('NA imputed')
inputfile = inputdata.InputFile.set_columns(inputfile)
print('Columns selected')
inputdata.InputFile.get_summary(inputfile)

# check your template extension

from hostedcatalog.checkfile import check_ext

# upload template file or hit enter to use default structure
from hostedcatalog.outputdata import OutputFile

# use template.xlsx file for testing
data = str(input('\nPaste TEMPLATE PATH \nas .xls or .xlsx\nor HIT ENTER to use default: '))\
            .replace('"', '')
if check_ext(data):
    outputfile = OutputFile.fromtemplate()
    print('File extension is correct. Uploading...')
else:
    outputfile = inputfile
    print('D.E.F.A.U.L.T!\nOutput File == Input File')

print(outputfile.head())

# here further work with template structure or default structure
if check_ext(data) == False:
    newcat = outputfile
else:
    newcat = inputfile.join(outputfile, how='left', lsuffix='o_')
    for ncolumn in newcat:
        if ncolumn not in inputfile.columns:
            print('\nFor column: ', ncolumn, '\nType one of following columns or X to loop over:\n', inputfile.columns)
            try:
                newcat[ncolumn] = newcat[str(input('Data from column: ')).upper()]
            except KeyError:
                print('\nKeyError!')
                for ocolumn in inputfile.columns:
                    print('\nFor ', ncolumn, ' apply values of ', ocolumn, '?\nPaste y or n ')
                    if input('y/n').lower() != 'y':
                        continue
                    else:
                        newcat[ncolumn] = inputfile[ocolumn]
                        break


    for column in newcat:
        if column in inputfile.columns:
            newcat = newcat.drop([column], axis=1)
            print(column, ' deleted')
    print(newcat.head())

newcat[str(input('Insert name of new column: '))] = newcat.apply(lambda _: '', axis=1)  # create new empty column
# newcat['MIME_LRG'] = outputdata.OutputFile.mime_lrg(newcat)  # create mime column and insert clean data

# save new catalog to newly created directory
new_folder(newcat)
