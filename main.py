import pandas as pd
from hostedcatalog.directory import Directory

# create new folder for new catalog version or use current directory
new_folder = Directory()
Directory.set_directory(new_folder)


# import your data from .xlsx or .xls file
from hostedcatalog import inputdata

while True:
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
data = str(input('Paste the PATH of your \nOUTPUT TEMPLATE file as EXCEL: ')).replace('"', '')
check_ext(data)

# upload template file or hit enter to use default structure
from hostedcatalog import outputdata
#newcat = OutputFile.from_file()
#newcat = newcat.cat_join(inputfile)

#newcat = outputdata.OutputFile.new_column(newcat) #not working
#newcat['MIME_LRG'] = outputdata.OutputFile.mime_lrg(newcat) # not working

#new_folder(inputfile)
