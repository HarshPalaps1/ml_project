from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."

#this function will return list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        ## read the object and replace "\n" with " "
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="student_exam_performance_prediction",
    version="0.0.1",
    author="harsh",
    author_email="harshpal@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)