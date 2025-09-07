from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
#   this funtion will return the list of requirements
         requirements=[]
         with open(file_path) as file_obj:
             requirements=file_obj.readlines()
             requirements=[req.replace("\n"," ") for req in requirements]

             if HYPEN_E_DOT in requirements:
                    requirements.remove(HYPEN_E_DOT)
         return requirements
# talking about setup we must say that it tells about metadata of project
setup(
    name='MLPROJECT',
    version='0.0.1',
    author='harshawardhan',
    author_email='thoratharshavardhan1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)
# their must be  relation between the setup and requirements