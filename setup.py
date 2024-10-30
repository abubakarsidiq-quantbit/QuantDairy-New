<<<<<<< HEAD
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quantdairy/__init__.py
from quantdairy import __version__ as version

setup(
	name="quantdairy",
	version=version,
	description="quantdairy",
	author="quantdairy",
	author_email="21pradipjadhav@gmail.com",
=======
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dairy/__init__.py
from dairy import __version__ as version

setup(
	name='dairy',
	version=version,
	description='Dairy modules',
	author='Dexciss Technology Pvt Ltd',
	author_email='dexciss',
>>>>>>> a83cf1a336a2383ac7b71f630883ddfcd584d6e3
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
