
if __name__ == '__main__':

    def example2():

        from pyigrf.pyigrf import GetIGRF
        from scipy import arange, arcsin, rad2deg

        xlat = -11.95
        xlon = 283.13
        year = 2004.75
        altlim = [90, 500.]
        altstp = 10.

        altbins = arange(altlim[0], altlim[1] + altstp, altstp)

        for i in range(len(altbins)):

            bn, be, bd, xl, icode = GetIGRF(xlat, xlon, altbins[i], year)

            # Horizontal component
            bh = (bn**2 + be**2)**.5
            # Total component
            ba = (bn**2 + be**2 + bd**2)**.5
            # Dip angle
            dip = rad2deg(arcsin(bd / ba))
            # Declination angle
            dec = rad2deg(arcsin(be / bh))

            print(i, altbins[i], bn, be, bd, xl, icode)
            print(bh, ba, dip, dec)
            print('')


    example2()
    