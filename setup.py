# Deploy in ppypi and we can setup or use it as a package manager

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path: str)-> List[str]:
    '''
    will return list of rquiremnts
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements        
        
setup(
    name= 'mlproject',
    version= '0.0.1',
    author= 'aditi',
    author_emai= 'aditisatsangi@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')   
)