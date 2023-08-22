from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in procurement/__init__.py
from procurement import __version__ as version

setup(
	name="procurement",
	version=version,
	description="Procurement module",
	author="Seyfert",
	author_email="procurement@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
