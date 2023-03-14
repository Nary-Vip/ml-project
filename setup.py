from setuptools import find_packages, setup
from typing import List

HYPHER_E = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHER_E in requirements:
            requirements.remove(HYPHER_E)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Naresh Kumar",
    author_email="nary2vip@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)