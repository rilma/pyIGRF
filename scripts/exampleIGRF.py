

def batch_igrf():

    from pyigrf.pyigrf import IGRFSub

    xlat = -11.95
    xlong = 283.13
    year = 2004.75
    height = 0.

    xl, icode, dip, dec = IGRFSub(xlat, xlong, year, height)

    print( xl, icode, dip, dec)

    #
    # End of 'batch_igrf'
    #####


def batch_get_igrf():

    from pyigrf.pyigrf import GetIGRF 

    xlat = -11.95
    xlon = 283.13
    year = 2004.75
    height = 0.

    bnorth, beast, bdown, xl, icode = GetIGRF(xlat, xlon, height, year)

    print( bnorth, beast, bdown, xl, icode )

    #
    # End of 'batch_get_igrf'
    #####


if __name__ == '__main__':

    batch_igrf()

    batch_get_igrf()

