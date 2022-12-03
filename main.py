import pandas as pd
from hostedcatalog import *
from hostedcatalog import directory, inputdata, outputdata
from hostedcatalog.directory import Directory
from hostedcatalog.outputdata import *

#new_folder = directory.Directory()
#directory.Directory.set_directory(new_folder)

inputfile = inputdata.InputFile()
inputfile = inputfile.impute_na()
inputfile = inputfile[inputfile['VOLUMEPRICE'] != 0]
inputfile = inputfile[inputfile['QTYAMOUNT'] == 1]
inputfile = inputfile.drop_duplicates(subset=['PARTNUM'])
inputfile = inputdata.InputFile.set_unit(inputfile)
inputfile = inputdata.InputFile.sup(inputfile)
inputfile = inputdata.InputFile.set_columns(inputfile)
inputdata.InputFile.get_summary(inputfile)

newcat = OutputFile.from_file()
newcat = newcat.cat_join(inputfile)

newcat = outputdata.OutputFile.new_column(newcat) #not working
newcat['MIME_LRG'] = outputdata.OutputFile.mime_lrg(newcat) # not working

new_folder(inputfile)
