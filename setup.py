
from glob import glob
from numpy.distutils.core import Extension, setup
from os.path import join

name = 'pyigrf'
sourcePath = 'source'

ext = []
for i in range(2):    
    modName = 'igrf' if i == 0 else 'get_igrf'     
    igrfSource = ['igrf_sub.pyf', 'igrf_sub.for'] if i == 0 else \
        ['get_igrf.pyf', 'get_igrf.for', 'igrf_sub.for'] 
    sources = []
    for src in igrfSource: sources.append(join(sourcePath, src))
    ext.append(Extension(name=modName, sources=sources, 
        f2py_options=['--quiet'], extra_f77_compile_args=['-w']))

igrfData = glob(join('data', '*.dat'))
igrfDataFiles = [(join(name, 'data'), igrfData)]


if __name__ == '__main__':

    setup(name=name, version='0.0.2', author='Ronald Ilma', 
        author_email='rri5@cornell.edu', description='IGRF model',
        packages=[name], ext_package=name, ext_modules=ext,
        data_files=igrfDataFiles)
