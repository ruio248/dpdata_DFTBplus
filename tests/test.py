import dpdata



def test_load():
    s = dpdata.LabeledSystem(r"C:\Users\Admin\Desktop\DFTB\dpdata_DFTBplus\tests\input.out", fmt= "dftbplus")
    assert len(s) == 1

if __name__ == "__main__":
    test_load()

