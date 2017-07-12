from setuptools import setup, find_packages

setup(
    name='colored_logger',
    packages=find_packages(),
    url='https://github.com/nimrodpar/colored_logger',
    description='A colored logger',
    long_description=open('README.md').read(),
    install_requires=[
        "logging>=0.0.0",
        ],
    include_package_data=True,
)
