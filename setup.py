""" brain 
"""

from setuptools import setup, find_packages

setup(
    name='brain',
    version='0.1',
    url='https://github.com/sinner-/brain',
    author='Sina Sadeghi',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'brain-manage = brain.cmd.manage:main',
            'brain = brain.cmd.brain:main',
        ]
    }
)
