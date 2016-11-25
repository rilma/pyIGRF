

from os.path import dirname, join, realpath
from os import sep
from .get_igrf import get_igrf

dataFolder = join(dirname(realpath(__file__)), 'data' + sep)

def GetIGRF(xlat=-11.95, xlon=283.13, height=0., year=2004.75):

    bnorth, beast, bdown, xl, icode = get_igrf(xlat, xlon, height, year, dataFolder)

    return bnorth, beast, bdown, xl, icode
