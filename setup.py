# setup.py file will be responsible in creating my  machine learning application as a package.
# you can also install this package in your project and use it .
#  setup.py file is basically a fie which you can use it as package and even deploy it on the python pypi so that every also can
# install and use it .

from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e.'
def get_requirement(file_path:str)->list[str]:
    '''
    This function will be return list of requirements.
    '''

    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirement=[req.replace("\n","")for req in requirement]


        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    


setup(
name='MLproject',
version='0.0.1',
author='sumit bavaskar',
author_email='sumitbawaskar68@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')
)

