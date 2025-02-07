"""
Setup
mar/2023
"""

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

requirements = []
for line in open('requirements.txt', encoding='utf-8'):
    li = line.strip()
    if not li.startswith('#'):
        requirements.append(line.rstrip())

VERSION = (0, 0, 5)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='sp_mpsp_divadmin',
    version=__version__,
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Divisão Administrativa das Áreas Regionais, GAEMAs, Redes Protetivas e Macroregiões e outras',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-geodata/sp_mpsp_divadmin',
    keywords='python, dados espaciais, geoprocessamento',
    # Python and Packages
    python_requires='>=3',
    install_requires=requirements,
    # Classificação
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
    # Entry
    # package_dir={'': 'sp_bh_pcj_2020_2035'},  # Our packages live under src but src is not a package itself
    # Quando são diversos módulos...
    packages=find_packages(),
    # Dados
    include_package_data=True,
    package_data={
        '': [
            'data/output/geo/*.7z',
            'data/output/tabs/*.csv',
        ]
    },
)
