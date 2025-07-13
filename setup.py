"""
The setup.py file is an essential part of packaging and
distributing Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more.
"""

from setuptools import find_packages, setup  # Importing setup tools for packaging
from typing import List  # For type hinting


def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of packages
    to be installed as dependencies.
    """
    requirementsList: List[str] = []  # Initialize empty list to hold requirements

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()  # Read all lines from requirements.txt

            for line in lines:
                requirement = line.strip()  # Remove leading/trailing whitespace

                # Skip editable install or invalid lines
                if requirement and not requirement.startswith('-e'):
                    requirementsList.append(requirement)

        return requirementsList

    except FileNotFoundError:
        print('requirements.txt file not found')
        raise()  # Raise the error again to stop execution


# Calling setup function to configure the package
setup(
    name="Network-Security-Project",             # Package name
    version="0.0.1",                              # Initial version
    author="Shreyank Sanjay Kasable",            # Author name
    author_email="shreyankkasabale@gmail.com",   # Author email
    packages=find_packages(),                    # Automatically find all packages/directories with __init__.py
    install_requires=get_requirements()          # List of dependencies fetched from requirements.txt
)
