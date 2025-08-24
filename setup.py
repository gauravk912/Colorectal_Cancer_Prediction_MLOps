from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='Colorectral-Cancer-Detection',
    version='0.1',
    author='Gaurav',
    packages=find_packages(),
    install_requires = requirements,
)