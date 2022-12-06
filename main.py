import pandas as pd
from hostedcatalog.directory import Directory

# create new folder for new catalog version or use current directory
new_folder = Directory()
Directory.set_directory(new_folder)

# import your data from .xlsx or .xls file
from hostedcatalog import inputdata, outputdata

# use test_input.xls for testing
while True:
    try:
        data = str(input('Paste the PATH of your \nINPUT file as EXCEL: ')).replace('"', '')
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
data = str(input('Paste again TEMPLATE PATH of your OUTPUT file as EXCEL\nor hit enter to use default structure: ')).replace('"', '')
if check_ext(data) == True:
    outputfile = OutputFile.fromtemplate()
else:
    outputfile = inputfile
    print('Output File == Input File')

print(outputfile.head())

# here further work with template structure or default structure
if check_ext(data) == False:
    newcat = outputfile
else:
    newcat = inputfile.join(outputfile, how='left', lsuffix='o_')
    for column in newcat:
        if column not in inputfile.columns:
            print('\nFor column: ', column, '\nChoose from:\n', inputfile.columns)
            try:
                newcat[column] = newcat[str(input('Data from column: ')).upper()]
            except KeyError:
                print('KeyError! Enter valid column name not case sensitive')

    for column in newcat:
        if column in inputfile.columns:
            newcat = newcat.drop([column], axis=1)
            print(column, ' deleted')
    print(newcat.head())

newcat[str(input('Insert name of new column: '))] = newcat.apply(lambda _: '', axis=1)  # create new empty column
newcat['MIME_LRG'] = outputdata.OutputFile.mime_lrg(newcat)  # create mime column and insert clean data

# save new catalog to newly created directory
new_folder(newcat)
