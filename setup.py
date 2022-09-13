from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="SAGAR NARULA"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()-> List[str]:
    """
    Description:This function is going to return list of requirement mention in requirement file

    return This function is going to return a list which contain libraries mentioned in the requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    Version=VERSION,
    author=AUTHOR,
    packages=find_packages(),  ### returns the list of packages where it will find __init__.py
    install_requires=get_requirements_list()

)


