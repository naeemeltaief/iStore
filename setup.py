from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in e_commerce/__init__.py
from e_commerce import __version__ as version

setup(
	name="e_commerce",
	version=version,
	description="e-commerce store",
	author="naeem eltaief",
	author_email="naeem.eltaief@me.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
