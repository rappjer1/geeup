import sys
import os
import sys
import setuptools
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from distutils.version import StrictVersion
from setuptools import __version__ as setuptools_version

if StrictVersion(setuptools_version) < StrictVersion('38.3.0'):
    raise SystemExit(
        'Your `setuptools` version is old. '
        'Please upgrade setuptools by running `pip install -U setuptools` '
        'and try again.'
    )
def readme():
    with open('README.md') as f:
        return f.read()
setuptools.setup(
    name='geeup',
    version='0.2.5',
    packages=find_packages(),
    url='https://github.com/samapriya/geeup',
    install_requires=['earthengine_api >= 0.1.175','requests >= 2.10.0','retrying >= 1.3.3','beautifulsoup4 >= 4.5.1',
    'pandas>=0.23.0','psutil>=5.4.5','requests_toolbelt >= 0.7.0','pytest >= 3.0.0','future >= 0.16.0',
    'google-cloud-storage >= 1.1.1','selenium>=3.13.0','pySmartDL==1.2.5;python_version<"3.4"',
    'pySmartDL>=1.3.1;python_version>"3.4"','pathlib>=1.0.1','lxml>=4.1.1','oauth2client>=4.1.3'],
    license='Apache 2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
    ),
    author='Samapriya Roy',
    author_email='samapriya.roy@gmail.com',
    description='Simple Client for Earth Engine Uploads with Selenium Support',
    entry_points={
        'console_scripts': [
            'geeup=geeup.geeup:main',
        ],
    },
)
