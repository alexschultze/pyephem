try:
    from setuptools import setup, Extension
except:
    from distutils.core import setup, Extension
from glob import glob

# The `pyephem' module is built from every .c file in the libastro
# directory plus ...

libastro_version = '3.7.2'
libastro_files = glob('libastro-%s/*.c' % libastro_version)

ext_modules = [
    Extension('_ephem', ['_ephem.c'] + libastro_files,
              include_dirs=['libastro-' + libastro_version],
              )]

setup(name = 'pyephem',
      version = '3.7.2a1',
      description = 'computational astronomy routines from XEphem',
      author = 'Brandon Craig Rhodes',
      author_email = 'brandon@rhodesmill.org',
      url = 'http://rhodesmill.org/brandon/projects/pyephem.html',
      py_modules = [ 'ephem' ],
      ext_modules = ext_modules)
