import pandas as pd
import os
import xlsxwriter

class OutputFile(pd.DataFrame):
    """Initialize a standard file or use fromtemplate method to upload a template"""
    @staticmethod
    def fromtemplate():
        data = str(input('Paste again TEMPLATE PATH of your \nOUTPUT file as EXCEL: ')).replace('"', '')
        while True:
            if data.endswith('xlsx'):
                template = pd.read_excel(data, engine='openpyxl')
                print('File format is .xlsx')
                break
            elif data.endswith('xls'):
                template = pd.read_excel(data, engine='xlrd')
                print('File format is .xls')
                break
            else:
                print('File format is invalid')
        return template

    def __init__(self, template, *args, **kwargs):
        pd.DataFrame.__init__(self, template, *args, **kwargs)
        print('Instance of OutputFile is created...')


    def mime_lrg(self):
        return self['PRODUCTIMAGE'].replace(to_replace=['small', 'sm'], value=['large', 'lrg'], regex=True)


if __name__ == '__main__':
    OutputFile.fromtemplate()
    OutputFile(template=inputfile)
