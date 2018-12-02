import importlib
import os

from setuptools import setup, find_packages


def _readme():
    _here = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(_here, 'README.md')).read()


mod = importlib.import_module('make_clean')
setup(
    name='make-clean',
    version=mod.__version__,
    author='Tomohiro NAKAMURA',
    author_email='quickness.net@gmail.com',
    url='https://github.com/jptomo/make-clean.py',
    description='A Cleanup Utility',
    long_description=_readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT License',
    packages=find_packages('.'),
    extras_require={
        'test': ['pytest', 'flake8', 'mypy'],
        'pypi': ['twine', 'wheel'],
    },
    entry_points={
        'console_scripts': [
            'make-clean = make_clean.__main__:main',
        ]
    },
)
