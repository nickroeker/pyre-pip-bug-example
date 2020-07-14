from setuptools import find_packages
from setuptools import setup

version = "0.1.0"

setup(
    name="my_package",
    version="0.1.0",
    author="Nic Kroeker",
    license="MIT",
    packages=find_packages("my_package"),
    install_requires=["pyre-check"],
)
