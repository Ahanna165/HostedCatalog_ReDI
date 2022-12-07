import pandas as pd
import os
import xlsxwriter

class OutputFile(pd.DataFrame):
    """Initialize a standard file or use fromtemplate method to upload a template"""
    @staticmethod
    def fromtemplate():
        while True:
            data = str(input('\nPATH of your OUTPUT TEMPLATE as EXCEL: ')).replace('"', '')
            if data.endswith('xlsx'):
                try:
                    template = pd.read_excel(data, engine='openpyxl')
                    print('File format is .xlsx', template.head())
                    return template
                except FileNotFoundError:
                    print('FileNotFoundError! Check file name !')

            elif data.endswith('xls'):
                try:
                    template = pd.read_excel(data, engine='xlrd')
                    print('File format is .xls', template.head())
                    return template
                except FileNotFoundError:
                    print('FileNotFoundError! Check file name !')

            else:
                print('File format is invalid! \nPaste the file path as .xlsx or .xls! ')
                continue

    def __init__(self, template, *args, **kwargs):
        pd.DataFrame.__init__(self, template, *args, **kwargs)
        print('Instance of OutputFile is created...')


    def mime_lrg(self):
        return self['PRODUCTIMAGE'].replace(to_replace=['small', 'sm'], value=['large', 'lrg'], regex=True)


if __name__ == '__main__':
    OutputFile.fromtemplate()
    OutputFile(template=inputfile)
