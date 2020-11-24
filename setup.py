# https://python-packaging.readthedocs.io
from setuptools import setup

setup(
    name="sunriselamp",
    version="0.1",
    description="a CLI to control an RGB lamp on a Raspberry Pi",
    # url                  =
    author="Jaime Liew",
    author_email="jaimeliew1@gmail.com",
    packages=["sunriselamp"],
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "sunriselamp=sunriselamp.cli:cli"
        ]
    },
)
