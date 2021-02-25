from setuptools import setup,find_packages
from os import path
from mrc_insar_common import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'MRC-InSAR-Common',
    version = __version__,
    author = 'Xinyao(Alvin) Sun',
    author_email = 'xinyao1@ualberta.ca',
    packages = ['mrc_insar_common', 'mrc_insar_common.data', 'mrc_insar_common.util'],
    install_requires = [
        'numpy'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
