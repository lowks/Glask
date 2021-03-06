from sys import argv

from setuptools import setup


install_requires = ['Flask>=0.10.1']
if 'develop' in argv[1:]:
    install_requires += ['pytest>=2.5.2']

setup(name='Glask', version='0.0.1', packages=['glask'], license='BSD',
      description='An extension for flask applications with best practices.',
      url='https://github.com/vamf12/Glask',
      install_requires=install_requires)
