from setuptools import setup, find_packages

setup(
    name='colored_logger',
    version='0.1',
    py_modules=['colored_logger.py'],
    packages=find_packages(),
    url='https://github.com/nimrodpar/colored_logger',
    description='A colored logger',
    long_description=open('README.md').read(),
    install_requires=[
        ],
    include_package_data=True,
)
