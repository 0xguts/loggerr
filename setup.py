from setuptools import setup, find_packages

setup(
    name="loggerr",
    version="0.1.0",
    author="0xguts",
    author_email="0xguts@nonexistingdomain.com",
    description="This package allows to help to log to file",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0xguts/loggerr",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)