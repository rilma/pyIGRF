

from os.path import dirname, join, realpath
from os import sep
from .igrf import igrf_sub
from .get_igrf import get_igrf


dataFolder = join(dirname(realpath(__file__)), 'data' + sep)


def IGRFSub(xlat=-11.95, xlong=283.13, year=2004.75, height=0.):

    xl, icode, dip, dec = igrf_sub(xlat, xlong, year, height, dataFolder)

    return xl, icode, dip, dec


def GetIGRF(xlat=-11.95, xlon=283.13, year=2004.75, height=0.):

    bnorth, beast, bdown, xl, icode = get_igrf(xlat, xlon, height, year, dataFolder)

    return bnorth, beast, bdown, xl, icode

