from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Najam Sheikh"
DESCRIPTION = "This is my first FSDS Nov ML Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    '''
    This function returns a list of libraries in requirements.txt
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(), # identifies the packages(folders) in the repository (eg. housing)
install_requires = get_requirements_list()

)

# if __init__name == "__main__":
#     print(get_requirements_list())