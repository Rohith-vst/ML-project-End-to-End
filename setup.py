from setuptools import find_packages,setup
# setup.py is used to use our ml project as package or application that we can install later if neededde
from typing import List
def get_requirments(file_path:str)->List[str] :
    '''
    this function will return the list of requirments
    '''
    requirements = []
    HYPEN_E_DOT  = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() 
        requirements = [req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT) 
    return requirements
 
setup(
name ='mlproject',
version ='0.0.1',
author = 'Rohith',
author_email = 'rohiththammu@gmail.com',
packages = find_packages(),
install_requires = get_requirments('requirements.txt'))