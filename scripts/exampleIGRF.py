

# def batch_igrf():

#     from pyigrf.pyigrf import IGRFSub

#     xlat = -11.95
#     xlong = 283.13
#     year = 2004.75
#     height = 0.

#     xl, icode, dip, dec = IGRFSub(xlat, xlong, year, height)

#     print( xl, icode, dip, dec)

#     #
#     # End of 'batch_igrf'
#     #####


def batch_get_igrf():

    from matplotlib.pyplot import figure, show
    from pyigrf.pyigrf import GetIGRF
    from scipy import arange 

    xlat = -11.95
    xlon = 283.13
    year = 2004.75
    height = 0.

    bnorth, beast, bdown, xl, icode = GetIGRF(xlat, xlon, height, year)

    print( bnorth, beast, bdown, xl, icode )

    #
    # End of 'batch_get_igrf'
    #####


# def heightProfile():

#     from matplotlib.pyplot import figure, show
#     from pyigrf.pyigrf import GetIGRF
#     from scipy import arange, nan, tile 
    
#     xlat = -11.95
#     xlon = 283.13
#     year = 2004.75
#     altlim = [0., 1000.]
#     altstp = 50.
    
#     altbins = arange(altlim[0], altlim[1] + altstp, altstp)
#     babs = tile(nan, len(altbins))
#     for i in range(len(altbins)):
#         bn, be, bd, xl, icode = GetIGRF(xlat, xlon, altbins[i], year)
#         babs[i] = (bn**2 + be**2 + bd**2)**.5

#     f = figure(figsize=(8,6))
#     pn = f.add_subplot(111)
#     pn.plot(babs, altbins, color='k')
#     show()


if __name__ == '__main__':

    ##batch_igrf()

    batch_get_igrf()

    #heightProfile()