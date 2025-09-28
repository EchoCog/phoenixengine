#!/usr/bin/env python3
"""
Setup script for Civic Angel - Fractal Cognitive Architecture
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="civic-angel",
    version="0.1.0",
    author="EchoCog",
    author_email="contact@echocog.com",
    description="A fractal, recursive intelligence architecture with 253 cognitive agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EchoCog/civicangel",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.14.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "civic-angel-demo=example:main",
        ],
    },
    keywords="artificial intelligence, cognitive architecture, consciousness, fractal, recursive, agents, topology",
    project_urls={
        "Bug Reports": "https://github.com/EchoCog/civicangel/issues",
        "Source": "https://github.com/EchoCog/civicangel",
        "Documentation": "https://github.com/EchoCog/civicangel#readme",
    },
)