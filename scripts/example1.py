if __name__ == '__main__':    

    def example1():

        from pyigrf.pyigrf import GetIGRF

        xlat = -11.95
        xlon = 283.13
        year = 2004.75
        alt = 250
        bn, be, bd, xl, icode = GetIGRF(xlat, xlon, alt, year)
        print(bn,be,bd)

    example1()