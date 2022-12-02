import pandas as pd
import os


class OutputFile(pd.DataFrame):
    """Initialize a standard file or use fromtemplate method to upload a template"""

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        print('Instance of OutputFile is created...')

    def __call__(self, path=input('Paste here the PATH of your template file as EXCEL\nor hit enter to use default: ')):
        # Split the extension from the path and normalise it to lowercase.
        self.path.strip('"')
        ext = os.path.splitext(self.path)[-1].lower()
        # Now we can simply use == to check for equality, no need for wildcards.
        if ext == ".xlsx":
            print(self.path, "is an {}}".format(ext))
        elif ext == ".xls":
            print(self.path, "is an {}}".format(ext))
        else:
            print(self.path, "is an unknown file format.")
        return pd.read_excel(self.path)

    def new_column(self):
        self[str(input('Name new column: '))] = self.apply(lambda _: '', axis=1)
        return self

    def mime_lrg(self):
        return self['PRODUCTIMAGE'].replace(to_replace=['small', 'sm'], value=['large', 'lrg'], regex=True)

    def cat_join(self, other):
        return self.join(other, how='left', lsuffix='o_')


if __name__ == '__main__':
    newcat = OutputFile()
