from setuptools import setup, find_packages

setup(
    name='colored_logger',
    packages=find_packages(),
    url='https://github.com/nimrodpar/colored_logger',
    description='A colored logger',
    long_description=open('README.md').read(),
    install_requires=[
        ],
    include_package_data=True,
)