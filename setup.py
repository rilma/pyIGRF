''' setup.py '''

# Verify the latest pip version
from os import system
system('pip install --upgrade pip')

# install required packages from PyPI
from pip import main as pip_main
pip_req = ['matplotlib', 'numpy', 'pandas', 'seaborn', 'scipy']
pip_main(['install'] + pip_req)

# set "develop" option
import setuptools

from glob import glob
from numpy.distutils.core import Extension, setup
from os.path import join

name = 'pyigrf'
sourcePath = 'source'
extra_compile_args = []
extra_f77_compile_args = ['-w', '-fno-align-commons']
ext = []

modName = 'get_igrf'
igrfSource = ['get_igrf.pyf', 'get_igrf.for', 'igrf_sub.for']
sources = []
for src in igrfSource: sources.append(join(sourcePath, src))
ext.append(Extension(name=modName, sources=sources, 
    f2py_options=['--quiet'], extra_compile_args=extra_compile_args, 
    extra_f77_compile_args=extra_f77_compile_args))

igrfData = glob(join('data', '*.dat'))
igrfDataFiles = [(join(name, 'data'), igrfData)]


if __name__ == '__main__':

    setup(name=name, version='1.0.0', author='Ronald Ilma', 
        author_email='rri5@cornell.edu', description='IGRF model',
        packages=[name], ext_package=name, ext_modules=ext,
        data_files=igrfDataFiles)
