import pandas as pd
import xlwings
import xlrd


class InputFile(pd.DataFrame):
    """instance, data ingestion, data inspection and data cleaning of output file"""

    def __init__(self, df, *args, **kwargs):  # data will ingest excel file
        pd.DataFrame.__init__(self, df, *args, **kwargs)
        print('Instance created: Rows, Columns', self.shape)

    def get_summary(self):  # inspect data for NA esp. unspsccode and coo
        print('COLUMNS: \t\tNA')
        print(self.isna().sum())

    def impute_na(self):  # imputes mode value inside of groups by level2
        self['UNSPSCCODE'] = self.groupby('LEVEL2')['UNSPSCCODE'].fillna(self['UNSPSCCODE'].mode()[0])
        self['COO'] = self.groupby('LEVEL2')['COO'].fillna(self['COO'].mode()[0])
        return self

    def set_columns(self):  # extracts only columns of interest
        return self[
            ['PARTNUM', 'PTITLE', 'QTYAMOUNT', 'VOLUMEPRICE', 'PRODUCTIMAGE', 'PAGELINK', 'UNITS', 'PRODUCTWEIGHT',
             'UNSPSCCODE', 'ECLASS']]

    def set_unit(self):  # renames units to ISO
        self['UNITS'] = self['UNITS'].str.upper()
        self['UNITS'] = self['UNITS'].replace(['EACH'], 'C62')
        self['UNITS'] = self['UNITS'].replace(['METER'], 'MTR')
        print(self['UNITS'].value_counts())
        return self

    def sup(self):  # cleans special characters
        self['PTITLE'] = self['PTITLE'].replace(
            to_replace=['</sup>/', '</sup>', '<sup>&reg;', '<sup>', '<sup style="font-size:6pt;', '">'], value=' ',
            regex=True)
        return self


if __name__ == "__main__":
    InputFile(df)

