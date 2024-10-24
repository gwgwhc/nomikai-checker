from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nomikai_checker",
    version="4.0.1",
    author="gwgwhc",
    description="Check if it's time for nomikai - if the Gods will it.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/gwgwhc/nomikai-checker",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    'console_scripts': [
        'nomikai_checker=nomikai_checker.__main__:main',
    ],
    },
    install_requires=[
        "PySimpleGUI<=4.60.5", # version without license issues
    ],
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
