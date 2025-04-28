from setuptools import setup, find_packages

setup(
    name='montecarlo_simulator',
    version='0.1',
    packages=find_packages(),
    description='Monte Carlo Simulator for dice-based games',
    author='Your Name',
    install_requires=[
        'numpy',
        'pandas'
    ]
)