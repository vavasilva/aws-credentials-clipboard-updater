from setuptools import setup, find_packages

setup(
    name='awscreds',
    version='1.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'awscreds=awscreds.cli:main',
        ],
    }
)
