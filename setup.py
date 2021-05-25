from setuptools import setup, find_packages

from codecs import open

with open("README.md") as read:
    l_descr = read.read()

setup(
    name="optake",
    version="0.1.3",
    description="Opt lib",
    long_description=l_descr,
    long_description_content_type="text/markdown",
    url="https://github.com/MrZloHex/optake.git",
    author="MrZloHex",
    author_email="zlo.alex.it@gmail.com",
    license="MIT",
    packages=["optake"],
    include_package_data=True,
    install_requires=[]
)
