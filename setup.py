from setuptools import setup

setup(
    name='repoready',
    version='0.1.0',
    py_modules=['repoready'],
    entry_points={
        'console_scripts': [
            'repoready=repoready:main',
        ],
    },
)
