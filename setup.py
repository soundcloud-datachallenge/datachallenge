from setuptools import setup

setup(
    name='datachallenge',
    version='0.1',
    packages=['challenge'],
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=['sortedcontainers'],
    scripts = ['challenge/mapper.py', 'challenge/reducer.py'],
)