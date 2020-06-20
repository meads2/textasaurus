from setuptools import setup, find_packages
from pathlib import Path

long_desc = Path('README.md').read_text()

setup(
    name="textasaurus", # Replace with your own username
    version="0.1.0",
    author="Matt Eads",
    author_email="matteads2@example.com",
    description="A simple AWS application for extracting text from PDFs using the cloud",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/meads2/textasaurus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['textasaurus=textasaurus.__main__:textasaurus']},
    python_requires='>=3.6'
)