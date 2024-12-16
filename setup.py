from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements_ = []
    with open(file_path) as f:
        requirements_ = f.readlines()
        requirements_ = requirements_.replace('\n','')
        return requirements_

setup( 
    name='Diamond Price Prediction', 
    version='0.0.1', 
    description='A Diamond Price Prediction', 
    author='Shivam Kashyap', 
    author_email='shivam.kashyap0121@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
) 