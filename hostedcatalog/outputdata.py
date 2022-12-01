import pandas as pd

class OutputFile(pd.DataFrame):
    """Initialize a standard file or use fromtemplate method to upload a template"""

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        print('Instance of OutputFile is created...')

    @classmethod
    def fromtemplate(cls, path=input('Paste here the PATH of your template file as EXCEL: ')):
        return pd.read_excel(path)

    def new_column(self):
        self[str(input('Nname new column: '))] = self.apply(lambda _: '', axis=1)
        return self

    def mime_lrg(self):
        return self['PRODUCTIMAGE'].replace(to_replace=['small', 'sm'], value=['large', 'lrg'], regex=True)

    def cat_join(self, other):
        return self.join(other, how='left', lsuffix='o_')


