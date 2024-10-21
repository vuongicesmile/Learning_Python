class NguoiVietNam:
    def __init__(self, cao, nang):
        self.cao = cao
        self.nang = nang
    def chay(self):
        print('dang chay')
    def ngu(self):
        print('dang ngu')

nguoi1 = NguoiVietNam(1,6)
nguoi1.cao = 2
print(nguoi1.chay())