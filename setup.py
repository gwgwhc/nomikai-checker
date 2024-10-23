from setuptools import setup, find_packages

# Read the README file for a long description (optional but recommended)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nomikai_checker",
    version="4.0.0",
    author="gwgwhc",
    description="Check if it's time for nomikai - if the Gods will it.",
    url="https://github.com/gwgwhc/nomikai-checker",
    packages=find_packages(),
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    entry_points={
    'console_scripts': [
        'nomikai_checker=nomikai_checker.__main__:main',
    ],
    },
    install_requires=[
        "PySimpleGUI>=4.0",  # External dependencies required for the project
    ],
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
