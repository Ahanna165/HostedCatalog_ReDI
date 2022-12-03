import pandas as pd
import os
import xlsxwriter

class OutputFile(pd.DataFrame):
    """Initialize a standard file or use fromtemplate method to upload a template"""

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        print('Instance of OutputFile is created...')

    @classmethod
    def from_file(cls, template=str(input('Paste the excel path ').strip('"'))):
        return pd.read_excel(template)

    def new_column(self):
        self[str(input('Name new column: '))] = self.apply(lambda _: '', axis=1)
        return self

    def mime_lrg(self):
        return self['PRODUCTIMAGE'].replace(to_replace=['small', 'sm'], value=['large', 'lrg'], regex=True)

    def cat_join(self, other):
        return self.join(other, how='left', lsuffix='o_')

if __name__ == '__main__':
    newcat = OutputFile.from_file()