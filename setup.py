from setuptools import setup, find_packages

setup(
    name="caesartool",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "caesartool=caesartool.cli:main"
        ]
    },
    author="Kiran Patel",
    description="Kali Linux style Caesar Cipher tool",
)
