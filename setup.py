from setuptools import setup
from codecs import open # To use a consistent encoding
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

setup(name='sage_sample',
    version=version,
    description="Basic Sage Optional Package",
    long_description=long_description,
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='sagemath',
    #keywords='sagemath combinatorics geometry symbolic dynamics',
    author='Sebastien Labbe',
    author_email='slabbe@ulg.ac.be',
    url='https://github.com/nthiery/sage_sample',
    license = "GPL",
    packages=['sage_sample']
)

