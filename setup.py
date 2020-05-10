import os
from setuptools import find_packages, setup


# This allows setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='project', # name of your library
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    description='My API Wrapper',
    long_description='You can use Python file API to load your README here',
    author='Petar Gitnik',
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
