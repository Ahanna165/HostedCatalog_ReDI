import pandas as pd
from hostedcatalog import *
from hostedcatalog import directory, inputdata, outputdata
from hostedcatalog.directory import Directory
from hostedcatalog.outputdata import *
import openpyxl

#new_folder = directory.Directory()
#directory.Directory.set_directory(new_folder)

data = str(input('Paste here the PATH of your input file as EXCEL: ')).replace('"', '')
while True:
    if data.endswith('xlsx'):
        df = pd.read_excel(data, engine='openpyxl')
        print('File format is .xlsx')
        break
    elif data.endswith('xls'):
        df = pd.read_excel(data, engine='xlrd')
        print('File format is .xls')
        break
    else:
        print('File format is invalid')

print(df.head())

#inputfile= InputFile(df)
#inputfile = InputFile(inputfile)
#inputfile = inputfile[inputfile['VOLUMEPRICE'] != 0]
#inputfile = inputfile[inputfile['QTYAMOUNT'] == 1]
#inputfile = inputfile.drop_duplicates(subset=['PARTNUM'])
#inputfile = inputdata.InputFile.set_unit(inputfile)
#inputfile = inputdata.InputFile.sup(inputfile)
#inputfile = inputdata.InputFile.set_columns(inputfile)
#inputdata.InputFile.get_summary(inputfile)

#newcat = OutputFile.from_file()
#newcat = newcat.cat_join(inputfile)

#newcat = outputdata.OutputFile.new_column(newcat) #not working
#newcat['MIME_LRG'] = outputdata.OutputFile.mime_lrg(newcat) # not working

#new_folder(inputfile)
