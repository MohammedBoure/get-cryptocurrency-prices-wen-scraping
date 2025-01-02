from setuptools import setup, find_packages

long_description = ""
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except (FileNotFoundError, UnicodeDecodeError):
    long_description = "A description of the package could not be loaded."

setup(
    name="PriceFlow",
    version="0.1",
    packages=find_packages(),
    install_requires=[ 
        "requests>=2.31.0",
    ],
    author="MohammedBoure",
    author_email="mohamadbormoz2@gmail.com",
    description="This script is used to get the current prices of cryptocurrencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohammedBoure/get-cryptocurrency-prices-wen-scraping",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    py_modules=["PriceFlow"],
)
