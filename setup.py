#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "pillow",
    "numpy",
]

setup_requirements = []

test_requirements = [
    "tox",
    "flake8",
    "black",
    "mypy",
    "isort",
    "pytest",
]

dev_requirements = ["bump2version", "twine"]

setup(
    author="Spencer Bliven",
    author_email="spencer.bliven@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Convert pixel images to diamond art templates",
    entry_points={
        "console_scripts": [
            "diamond_art=diamond_art.cli:main",
        ],
    },
    install_requires=requirements,
    extras_require={
        "tests": test_requirements,
        "dev": dev_requirements + test_requirements,
    },
    license="BSD license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="diamond_art",
    name="diamond_art",
    packages=find_packages(include=["diamond_art", "diamond_art.*"]),
    package_data={
        "": ["*.md", "CHANGELOG.md"],
        "diamond_art.data.fonts.Noto_Sans_Symbols": ["*.ttf"],
    },
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/sbliven/diamond-art",
    version="0.1.0",
    zip_safe=True,
)
