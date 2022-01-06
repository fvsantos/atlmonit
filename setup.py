from setuptools import setup, find_packages

setup(
    name="atlmonit_1",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "atlmonit_2 = atlmonit.main:cli",
        ],
    },
)
