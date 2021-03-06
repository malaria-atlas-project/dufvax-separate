from setuptools import setup
from numpy.distutils.misc_util import Configuration
import os
config = Configuration('dufvax',parent_package=None,top_path=None)
config.add_extension(name='flikelihood',sources=['dufvax/flikelihood.f'])
config.packages = ["dufvax"]

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**(config.todict()))