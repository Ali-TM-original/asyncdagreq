from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='asyncdagreq',
    version='1.0',
    description='An async wrapper made in Python for Dagpi.',
    long_description=long_description,
    url='https://github.com/Ali-TM-original/asyncdagreq',
    author='Ali-TM-original',
    license='MIT',
    packages=['asyncdagreq'],
    install_requires=['aiohttp'],
    requirements=requirements,
    zip_safe=False,
)
