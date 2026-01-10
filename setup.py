from setuptools import setup, find_packages

VERSION = "25.10.30"

INSTALL_REQUIRES = []
EXCLUDE_PACKAGES = []

setup(
    name="openarm_idl_py",
    version=VERSION,
    author="oymotion",
    author_email="info@oymotion.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="BSD-2-Clause",
    description="openarm idl",
    url="",
    packages=find_packages(where="src", exclude=EXCLUDE_PACKAGES),
    package_dir={"":"src"},
    install_requires=INSTALL_REQUIRES
)