from pathlib import Path

from setuptools import find_packages
from setuptools import setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with open(DOCS_PATH, encoding="utf-8") as f1:
        with open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="SydneyGPT",
    version="0.11.6",
    license="GNU General Public License v2.0",
    author="Rafael Calleja",
    author_email="rafaelcalleja@gmail.com",
    description="Reverse engineered Sydney Bing Chat API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/rafaelcalleja/SydneyGPT",
    project_urls={"Bug Report": "https://github.com/rafaelcalleja/SydneyGPT/issues/new"},
    entry_points={
        "console_scripts": [
            "sydney-gpt = SydneyGPT:main",
        ],
    },
    install_requires=[
        "EdgeGPT>=0.8.2",
    ],
    long_description=open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["SydneyGPT"],
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
