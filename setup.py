from setuptools import setup,find_packages
from mrc_insar_common import __version__

setup(
    name = 'MRC-InSAR-Common',
    version = __version__,
    author = 'Xinyao(Alvin) Sun',
    author_email = 'xinyao1@ualberta.ca',
    packages = ['mrc_insar_common'],
    install_requires = [
        'numpy'
    ]
)
