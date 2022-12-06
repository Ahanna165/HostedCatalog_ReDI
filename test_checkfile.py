from hostedcatalog.checkfile import check_ext


def test_check_1good_ext():
    assert check_ext("\!!!_PY NOTEBOOKS\Input files\productCatalogExpanded.xls") == True

def test_check_2good_ext():
    assert check_ext("\!!!_PY NOTEBOOKS\Input files\productCatalogExpanded.xlsx") == True

def test_check_bad_ext():
    assert check_ext("\!!!_PY NOTEBOOKS\protocoll.txt") == False


