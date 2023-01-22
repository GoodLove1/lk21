#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = ['lk21', 'lk21.extractors', 'lk21.thirdparty']
package_data = {'': ['*']}
install_requires = ['questionary', 'bs4',
                    'requests', 'requests-cache', 'colorama']
entry_points = {'console_scripts': ['lk21 = lk21.cli:main']}

setup(name='lk21',
      version='1.5.4',
      description='cari anime dan film subtitle Indonesia',
      author='Val',
      author_email='kingworker001@gmail.com',
      url='https://github.com/GoodLove1',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.8',
      )
