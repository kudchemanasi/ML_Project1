from typing import List,Dict
from setuptools import setup

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements
    mention in requirements.txt file

    return This function is going to return a list which containsname of libraries mentioned in requirements.txtfile 

    """
     
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readline()

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Manasi Kudche"
DESCRIPTION = "This is a first FSDS NOV Batch Machine Learning Project"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

setup(
    name= PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()

)

